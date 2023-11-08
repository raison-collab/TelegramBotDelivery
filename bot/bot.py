import asyncio
from . import bot, dp, logger


def on_startup(_):
    print(f'Бот запущен!')


async def on_shutdown(_):
    pass


async def main():
    await dp.start_polling(bot)


def run():
    logger.success('Bot Started')
    asyncio.run(main())
