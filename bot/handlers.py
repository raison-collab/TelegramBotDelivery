from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from enums import URLS, PATH

from . import dp, parser, logger, accept_control
from .keyboards import start_keyboard
from .models import User


@dp.message(CommandStart())
async def start_command(message: Message):
    user = User.from_message(message)
    accept_control.append_user(user)
    logger.debug(f'Пользователь: {user} начал работу с ботом')
    await message.answer('Привет. Вот тебе клава для управления', reply_markup=start_keyboard)


@dp.message(Command('ЯндексЛавка'))
async def yandex_lavka_command(message: Message):
    data = parser.parse_yandex_lavka(URLS.LAVKA.value, str(PATH.COOKIES.value))
    logger.info(f'Получены данные ЯндексЛавка | data={data}')
    text = "\n".join([f'<b>{key}</b>: {data[key]}' for key in data])
    await message.answer(text)
