import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from dotenv import dotenv_values
from loguru import logger

if not os.path.exists(".env"):
    with open(".env", mode="w") as file:
        new_token = input("Введите токен бота: ")
        file.write(f"TOKEN={new_token}")

config = dotenv_values('.env')

bot = Bot(
    token=config['TOKEN'],
    parse_mode=ParseMode.HTML
)

dp = Dispatcher(
    bot=bot
)

from .bot import run
