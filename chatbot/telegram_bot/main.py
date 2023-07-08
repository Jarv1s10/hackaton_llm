import os
import requests

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# ------------- ENV VARIABLES -------------

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# ------------- WEBSERVER -------------
API_HOST = 'api'
HEADERS = {
    'accept': 'application/json'
}

# ------------- TELEGRAM OBEJCTS -------------
bot = Bot(token=TELEGRAM_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# ------------- SESSION CLASS -------------

class UserSession:
    def __init__(self, user_id: int, history: list[tuple]):
        self.user_id = user_id
        self.history = history

# ------------- HANDLERS -------------

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    session = UserSession(user_id, [])
    dp.bot.data.update({"session": session})
    await message.reply("Hey! This bot was created to answer all your questions about RevenueGrid! Let's get started. Ask me something:")


@dp.message_handler(commands=['help'])
async def start_handler(message: types.Message):
    await message.reply("This bot was created to answer all your questions about RevenueGrid! Ask your question below! To restart a conversation, use /restart command.")

@dp.message_handler(commands=['test'])
async def start_handler(message: types.Message):
    r = requests.get(f'http://{API_HOST}:8000/', headers=HEADERS)
    if r.status_code != 200:
        await message.reply(f'Something went wrong with chat request =(\nStatus code: {r.status_code}')
    else:
        msg = r.json()['message']
        await message.reply(f'Everything is good! API response: {msg}')


@dp.message_handler(commands=['restart'])
async def example_handler(message: types.Message):
    session: UserSession = dp.bot.get('session')
    if session is None:
        await message.reply("Session not found. Please use the /start command first.")
        return

    session.history = []
    dp.bot.data.update({"session": session})
    await message.reply(f"Session is reset. All previous conversation is forgotten.")


@dp.message_handler()
async def text_message_handler(message: types.Message):
    session: UserSession = dp.bot.get('session')
    if session is None:
        await message.reply("Session not found. Please use the /start command first.")
        return

    bot_message = await message.reply('Thinking...')

    data = {
        'user_message': message.text.strip(),
        'history': session.history
    }
    r = requests.post(f'http://{API_HOST}:8000/chat/', json=data, headers=HEADERS)
    if r.status_code != 200:
        await bot_message.edit_text(f'Something went wrong with chat request =(\nStatus code: {r.status_code}')
        return

    chat_response = r.json()
    llm_answer, sources = chat_response['llm_answer'], chat_response['sources']

    sources = set(f"[{s['doc_title']}]({s['doc_url']})" for s in sources)
    sources = 'Documentation sources:\n' + '\n'.join(sources)
    display_answer = llm_answer + '\n------------------------------------------\n' + sources
    await bot_message.edit_text(display_answer, parse_mode='Markdown')

    session.history.append((message.text, llm_answer))
    dp.bot.data.update({"session": session})


if __name__ == '__main__':
    print('Telegram bot started. Visit @RevenueGrid_insider_bot')
    executor.start_polling(dp)
