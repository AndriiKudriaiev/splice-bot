import config
import logging
from aiogram import Bot, Despatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot=Bot(token=config.TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(Command=["start"])
async def start_command(message: types.Message):
    await message.reply("Hi")



if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)

