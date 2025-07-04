import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ParseMode
import asyncio
import os

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

ADMIN_ID = os.getenv("ADMIN_ID")

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if str(message.from_user.id) == str(ADMIN_ID):
        await message.answer("👑 Добро пожаловать, Юсуф!\n\n🚀 BORZ.AI запускается...\n🤖 ИИ активирован\n🔗 65 ботов и 30 подботов подключено\n📡 Сеть готова к работе!\n\n👉 Нажми /menu для управления")
    else:
        await message.answer("⚠️ Доступ ограничен.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
