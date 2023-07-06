from aiogram import Bot, Dispatcher, executor, types
import json
import re
from llama_cpp import Llama

bot = Bot(token = "6048201860:AAGSNZTxpeXUI5WBglEmp3B7dvo3uVIZsWQ")
dp = Dispatcher(bot)

print("Loading model...")
llm = Llama(model_path='models/ggml-vic7b-q5_1.bin')
print("Model loaded")

@dp.message_handler(commands = ['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hey! This bot was created to answer all your questions about RevenueGrid! Let's get started. Ask me something:")


@dp.message_handler()
async def gpt(message: types.Message):
    # generating an answer for given user's message
    ouptut = llm("Question: {} Answer:".format(message.text),
                 max_tokens=150,
                 stop=['\n', 'Question:', "Q:"],
                 echo=True
    )
    # returning reply to users message
    await message.reply(re.findall(r"Answer:\s+(.*)", ouptut['choices'][0]['text'])[0])


if __name__ == "__main__":
    # executor.start_polling(dp)
    print('hello')