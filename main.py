import os

from boltiotai import openai
from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from example import example

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()

openai.api_key = os.getenv("OPENAI_API_KEY")

example()


@dp.message(CommandStart())
async def welcome(message: types.Message):
  await message.reply('Hello! I am Recipe Generator BOT programmed by Nimesh. Give me the name of the ingredients that you have :)')


@dp.message()
async def gpt(message: types.Message):
  messages=[{
     "role": "system",
     "content": "You are a helpful assistant"
    }, {
     "role":
     "user",
     "content":
     f"Suggest a recipe using the items listed as available. Make sure you have a nice name for this recipe listed at the start. Also, include a funny version of the name of the recipe on the following line. Then share the recipe in a step-by-step manner. In the end, write a fun fact about the recipe or any of the items used in the recipe. Here are the items available: {message.text}, Haldi, Chilly Powder, Tomato Ketchup, Water, Garam Masala, Oil"
    }]

  response = openai.chat.completions.create(model="gpt-3.5-turbo", messages=messages)

  await message.reply(response['choices'][0]['message']['content'])

async def main():
  await dp.start_polling(bot)

if __name__ == "__main__":
  asyncio.run(main())