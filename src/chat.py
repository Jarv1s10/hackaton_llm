import os
from typing import Callable

from pydantic import BaseModel
import weaviate

import langchain
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Weaviate
from langchain.llms import OpenAI
# from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationTokenBufferMemory, ConversationBufferMemory
from langchain.cache import InMemoryCache
from langchain.callbacks import get_openai_callback
from langchain.schema import Document
# from langchain.schema.messages import SystemMessage, HumanMessage, AIMessage
from langchain.prompts.prompt import PromptTemplate

from dotenv import load_dotenv

load_dotenv()


OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
WEAVIATE_API_KEY = os.getenv('WEAVIATE_API_KEY')
WEAVIATE_URL = os.getenv('WEAVIATE_URL')

client = weaviate.Client(
    url=WEAVIATE_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY),
)

db = Weaviate(client, 'RGDocs', 'text',
              OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY),
              by_text=False, attributes=['doc_title', 'doc_url'])

langchain.llm_cache = InMemoryCache()
LLM = OpenAI(cache=True, model_name="text-davinci-003", openai_api_key=OPENAI_API_KEY, max_tokens=1500)
LLM_TOKEN_LIMIT = LLM.max_context_size - 500

with open(os.path.join(os.path.dirname(__file__), 'prompt_templates', 'system_message_template.txt'), 'r') as f:
    SYSTEM_MESSAGE_TEMPLATE = PromptTemplate.from_template(f.read())

with open(os.path.join(os.path.dirname(__file__), 'prompt_templates', 'condense_question_template.txt'), 'r') as f:
    CONDENSE_QUESTION_TEMPLATE = PromptTemplate.from_template(f.read())


class ChatInfo(BaseModel):
    user_message: str
    history: list[tuple[str, str]]

def reduce_tokens_below_limit(docs: list[Document], max_tokens_limit: int, token_len_func: Callable[[str], int]) -> list[Document]:
    num_docs = len(docs)
    tokens = [
        token_len_func(doc.page_content)
        for doc in docs
    ]
    token_count = sum(tokens[:num_docs])
    while token_count > max_tokens_limit:
        num_docs -= 1
        token_count -= tokens[num_docs]

    return docs[:num_docs]


def get_chat_answer(chat: ChatInfo):
    memory = ConversationTokenBufferMemory(llm=LLM, max_token_limit=LLM_TOKEN_LIMIT // 2)
    for inpt, out in chat.history:
        memory.save_context({'input': inpt}, {'output': out})

    history = memory.load_memory_variables({})['history']
    if history:
        condenced_question_prompt = CONDENSE_QUESTION_TEMPLATE.format(chat_history=history, question=chat.user_message)

        while True:
            print('Get condenced question:')
            with get_openai_callback() as cb:
                condenced_question = LLM.predict(condenced_question_prompt)
                print(cb)
            if condenced_question.strip():
                break
            print('RETRY...')
    else:
        condenced_question = chat.user_message

    relevant_docs = db.similarity_search(
        condenced_question,
        where_filter={
            'path': ["short_site_name"],
            'operator': 'Equal',
            'valueString': 'Sfcc'
        }
    )

    relevant_docs = reduce_tokens_below_limit(relevant_docs, LLM_TOKEN_LIMIT // 2, LLM.get_num_tokens)
    context = '\n\n'.join([doc.page_content for doc in relevant_docs])

    question_prompt = SYSTEM_MESSAGE_TEMPLATE.format(context=context, question=condenced_question)

    while True:
        print('Get answer to a question:')
        with get_openai_callback() as cb:
            llm_answer = LLM.predict(question_prompt)
            print(cb)
        if llm_answer.strip():
            break
        print('RETRY...')

    sources = [doc.metadata for doc in relevant_docs]
    return {'llm_answer': llm_answer, 'sources': sources}