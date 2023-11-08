from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger

from enums import Urls, Cookies
from loader import dp
from utils import Utils


@dp.message(Command('ЯндексЛавка'))
async def yandex_lavka_command(message: Message):
    data = Utils.parse_yandex_lavka(Urls.yandex_lavka.value, str(Cookies.yandex_lavka.value))
    logger.info(f'Получены данные ЯндексЛавка | data={data}')

    ans = ''

    for key in data:
        ans += f'<b>{key}</b>: {data[key]}\n'

    await message.answer(ans)
