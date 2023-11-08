import asyncio

from loguru import logger

from loader import dp, bot, config

import handlers


def on_startup(_):
    print(f'Бот запущен!')


async def on_shutdown(_):
    pass


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logger.success('Bot Started')
    asyncio.run(main())
