import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.filters import Command
from aiogram.types import Message

import config

bot = Bot(token=config.TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Открыть приложение", web_app=WebAppInfo(url="https://c7ea20020786.ngrok-free.app"))]
        ],
        resize_keyboard=True
    )
    await message.answer("Привет! Всё взаимодействие идёт через приложение", reply_markup=kb)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
   asyncio.run(main())
