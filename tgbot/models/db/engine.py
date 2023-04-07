from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker, AsyncEngine


def create_engine(url):
    return create_async_engine(url=url, pool_pre_ping=True)


async def proceed_schemas(engine: AsyncEngine, metadata: MetaData):
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)


def create_session(engine: AsyncEngine):
    return async_sessionmaker(bind=engine, class_=AsyncSession)
