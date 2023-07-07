import os
import asyncio

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text

import weaviate
import tiktoken

from langchain.text_splitter import RecursiveCharacterTextSplitter, TextSplitter
from langchain.schema import Document
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Weaviate
from langchain.llms import OpenAI, BaseLLM
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationTokenBufferMemory, ConversationSummaryBufferMemory

# ------------- ENV VARIABLES -------------

load_dotenv(os.path.join(os.path.dirname(__file__), os.pardir, '.env'))

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
WEAVIATE_API_KEY = os.getenv('WEAVIATE_API_KEY')
WEAVIATE_URL = os.getenv('WEAVIATE_URL')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# ------------- LLM OBJECTS -------------
client = weaviate.Client(
    url=WEAVIATE_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY),
)

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

db = Weaviate(client, 'RGDocs', 'text', embeddings, by_text=False)
db._query_attrs = [p['name'] for p in client.schema.get('RGDocs')['properties']]

# llm = OpenAI(openai_api_key=OPENAI_API_KEY)

class DummyLLM(BaseLLM):
    _tokenizer = tiktoken.encoding_for_model('gpt-3.5-turbo')

    def predict(self, text: str) -> str:
        text = text[text.find('Summaries:\n') + len('Summaries:\n'):]
        return text.split('\n')[0]

    def get_num_tokens(self, text):
        return len(self._tokenizer.encode(text))

    def _generate(
        self,
        prompts,
        stop = None,
        run_manager = None,
        **kwargs,
    ):
        """Run the LLM on the given prompts."""

    async def _agenerate(
        self,
        prompts,
        stop = None,
        run_manager = None,
        **kwargs,
    ):
        """Run the LLM on the given prompts."""

    def _llm_type(self) -> str:
        return "Return type of llm."

LLM = DummyLLM()
LLM_TOKEN_LIMIT = 4_000
SYSTEM_MESSAGE = \
"""You are an AI assistant for the Revenue Grid documentation.
You are given a question and extracted parts of product documentation. Provide a conversational answer to the question using the pieces of information provided.
If the question includes a request for code, provide a code block directly from the documentation.
If you don't know the answer, just say "Hmm, I'm not sure." Don't try to make up an answer.
If the question is not about Revenue Grid, politely inform them that you are tuned to only answer questions about Revenue Grid.
"""

# ------------- TELEGRAM OBEJCTS -------------
bot = Bot(token=TELEGRAM_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# ------------- SESSION CLASS -------------

class UserSession:
    def __init__(self, user_id: int, memory: ConversationTokenBufferMemory):
        self.user_id = user_id
        self.memory = memory

# ------------- HANDLERS -------------

# Handler for the "/start" command
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    memory = ConversationTokenBufferMemory(llm=LLM, max_token_limit=LLM_TOKEN_LIMIT // 2)
    session = UserSession(user_id, memory)
    dp.bot.data.update({"session": session})

    await dp.bot.send_message(chat_id=message.chat.id, text="Hey! This bot was created to answer all your questions about RevenueGrid! Let's get started. Ask me something:")

@dp.message_handler(commands=['help'])
async def start_handler(message: types.Message):
    await message.reply("Hey! This bot was created to answer all your questions about RevenueGrid! Let's get started. Ask me something:")

# Example handler that uses the session object
@dp.message_handler(commands=['example'])
async def example_handler(message: types.Message):
    # Retrieve the session object from the chat context
    session: UserSession = dp.bot.get('session')
    if session is None:
        await message.reply("Session not found. Please use the /start command first.")
        return

    # Access session properties
    user_id = session.user_id
    memory = session.memory
    # Perform actions based on the session data
    await message.reply(f"Session found for user ID: {user_id}. Chat history: {memory.load_memory_variables({})['history']}")

@dp.message_handler()
async def text_message_handler(message: types.Message):
    session: UserSession = dp.bot.get('session')
    if session is None:
        await message.reply("Session not found. Please use the /start command first.")
        return

    query = message.text
    history = session.memory.load_memory_variables({})['history'] + '\n' + f'Human: {query}'
    relevant_docs = db.similarity_search(history, by_text=False)

    while sum([LLM.get_num_tokens(doc.page_content) for doc in relevant_docs]) > LLM_TOKEN_LIMIT // 2:
        relevant_docs = relevant_docs[:-1]

    summaries = [doc.page_content for doc in relevant_docs]
    summaries = '\n'.join(summaries)

    sources = 'Sources:\n' + '\n'.join([f"[{doc.metadata['doc_title']}]({doc.metadata['doc_url']})" for doc in relevant_docs])

    prompt_to_llm = SYSTEM_MESSAGE + history + 'Summaries:\n' + summaries
    llm_answer = LLM.predict(prompt_to_llm)
    display_answer = llm_answer + '\n--------------\n' + sources

    session.memory.save_context({'input': query}, {'output': llm_answer})
    dp.bot.data.update({"session": session})

    await message.reply(display_answer, parse_mode='Markdown')

# Start the bot
if __name__ == '__main__':
    executor.start_polling(dp)
