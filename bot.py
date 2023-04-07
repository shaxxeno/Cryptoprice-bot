import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from tgbot.config import load_config
from tgbot import handlers
from tgbot.middlewares.config import ConfigMiddleware
from tgbot.middlewares.register_check import RegisterCheck
from tgbot.misc.commands import set_commands
from sqlalchemy.engine import URL
from tgbot.models.db.engine import create_engine, proceed_schemas, create_session
from tgbot.models.db.users import Base

logger = logging.getLogger(__name__)


async def on_startup(bot: Bot):
    await set_commands(bot)


def register_global_middlewares(dp: Dispatcher, config):
    dp.message.outer_middleware(ConfigMiddleware(config))
    dp.message.outer_middleware(RegisterCheck())
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

    dp.include_router(handlers.router)
    dp.startup.register(on_startup)

    register_global_middlewares(dp, config)
    postgres_url = URL.create(
        'postgresql+asyncpg',
        username=load_config().db.user,
        port=load_config().db.port,
        host=load_config().db.host,
        database=load_config().db.database,
        password=load_config().db.password
    )

    create_async_engine = create_engine(postgres_url)
    create_async_session = create_session(create_async_engine)
    await proceed_schemas(create_async_engine, metadata=Base.metadata)
    await dp.start_polling(bot, session_maker=create_async_session)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
