from email.mime import text
import os

from dotenv import load_dotenv

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import weaviate

import langchain
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Weaviate
from langchain.llms import OpenAI, FakeListLLM
from langchain.memory import ConversationTokenBufferMemory
from langchain.cache import InMemoryCache
from langchain.callbacks import get_openai_callback

try:
    from process_doc_page import process_doc_page
except ModuleNotFoundError:
    from .process_doc_page import process_doc_page

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
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
LLM = OpenAI(cache=True, model_name="text-davinci-003", openai_api_key=OPENAI_API_KEY, max_tokens=2000)
LLM_TOKEN_LIMIT = LLM.max_context_size

with open(os.path.join(os.path.dirname(__file__), 'system_message.txt'), 'r') as f:
    SYSTEM_MESSAGE = f.read()

app = FastAPI()


@app.get('/')
def test():
    return {'message': 'Hello from FastAPI'}

@app.get('/pages/')
def get_doc_sections_by_url(doc_url: str) -> list[dict]:
    result = (
        client.query.get('RGDocs', ['text', 'doc_title', 'doc_url'])
        .with_where({
            'path': ['doc_url'],
            'operator': 'Equal',
            'valueString': doc_url
        })
        .do()['data']['Get']['RGDocs']
        )
    if not result:
        raise HTTPException(status_code=404, detail=f"Item with {doc_url=} does not exist.")
    return result


@app.post('/pages/')
def add_doc_by_url(doc_url: str) -> list[str]:
    get_by_url = (
        client.query.get('RGDocs', ['text', 'doc_title', 'doc_url'])
        .with_where({
            'path': ['doc_url'],
            'operator': 'Equal',
            'valueString': doc_url
        })
        .do()['data']['Get']['RGDocs']
        )
    if get_by_url:
        raise HTTPException(status_code=400, detail=f"Item with {doc_url=} already exists.")

    docs = process_doc_page(doc_url)
    return db.add_documents(docs)


@app.put('/pages/')
def update_doc_sections_by_url(doc_url: str) -> list[str]:
    client.batch.delete_objects(
        'RGDocs',
        {
            'path': ['doc_url'],
            'operator': 'Equal',
            'valueString': doc_url
        })

    docs = process_doc_page(doc_url)
    return db.add_documents(docs)


@app.delete('/pages/')
def delete_doc_sections_by_url(doc_url: str, dry_run: bool = True) -> dict:
    return client.batch.delete_objects(
        'RGDocs',
        {
            'path': ['doc_url'],
            'operator': 'Equal',
            'valueString': doc_url
        },
        output='verbose',
        dry_run=dry_run)


class ChatInfo(BaseModel):
    user_message: str
    history: list


@app.post('/chat/')
def get_llm_model_answer(chat: ChatInfo):
    memory = ConversationTokenBufferMemory(llm=LLM, max_token_limit=LLM_TOKEN_LIMIT // 2)
    for inpt, out in chat.history:
        memory.save_context({'input': inpt}, {'output': out})
    relevant_docs = db.similarity_search(chat.user_message)

    while len(relevant_docs) > 1 and sum([LLM.get_num_tokens(doc.page_content) for doc in relevant_docs]) > LLM_TOKEN_LIMIT // 2:
        relevant_docs = relevant_docs[:-1]

    summaries = [doc.page_content for doc in relevant_docs]
    summaries = '\n'.join(summaries)

    history = memory.load_memory_variables({})['history']
    prompt_to_llm = '\n'.join([SYSTEM_MESSAGE, history, f'Human: {chat.user_message}', f'Summaries:\n{summaries}', 'AI: '])

    with get_openai_callback() as cb:
        llm_answer = LLM.predict(prompt_to_llm)
        print(cb)

    sources = [doc.metadata for doc in relevant_docs]

    return {'llm_answer': llm_answer, 'sources': sources}