import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from tgbot.config import load_config
from tgbot.handlers.user import user_router
from tgbot.middlewares.config import ConfigMiddleware
from tgbot.misc.commands import set_commands

# from tgbot.handlers.admin import admin_router

logger = logging.getLogger(__name__)


async def on_startup(bot: Bot):
    await set_commands(bot)


def register_global_middlewares(dp: Dispatcher, config):
    dp.message.outer_middleware(ConfigMiddleware(config))
    dp.callback_query.outer_middleware(ConfigMiddleware(config))


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    storage = MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(storage=storage)

    for router in [
        # admin_router,
        user_router,
    ]:
        dp.include_router(router)
        dp.startup.register(on_startup)

    register_global_middlewares(dp, config)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
