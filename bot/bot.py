import asyncio
from . import bot, dp, logger, handlers


def on_startup():
    logger.success('Bot Started')


def on_shutdown():
    logger.success('Bot Finished')


async def main():
    on_startup()
    await dp.start_polling(bot)


def run():
    asyncio.get_event_loop().run_until_complete(main())
    on_shutdown()
