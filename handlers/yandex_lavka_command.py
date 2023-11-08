from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger

from enums import PATH, URLS
from loader import dp
import parser


@dp.message(Command('ЯндексЛавка'))
async def yandex_lavka_command(message: Message):
    data = parser.parse_yandex_lavka(URLS.LAVKA.value, str(PATH.COOKIES.value))
    logger.info(f'Получены данные ЯндексЛавка | data={data}')

    ans = ''

    for key in data:
        ans += f'<b>{key}</b>: {data[key]}\n'

    await message.answer(ans)
