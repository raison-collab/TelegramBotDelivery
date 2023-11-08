from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from dotenv import load_dotenv, dotenv_values

config = dotenv_values('.env')

bot = Bot(
    token=config['TOKEN'],
    parse_mode=ParseMode.HTML
)

dp = Dispatcher(
    bot=bot
)
