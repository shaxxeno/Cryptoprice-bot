from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Awaitable, Any
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from tgbot.models.db.users import User


class RegisterCheck(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        session_maker: sessionmaker = data['session_maker']
        async with session_maker() as session:
            async with session.begin():
                result = await session.execute(select(User).where(User.user_id == event.from_user.id))
                user = result.one_or_none()

                if user:
                    pass
                else:
                    user = User(
                        user_id=event.from_user.id,
                        user_name=event.from_user.username
                    )
                    await session.merge(user)

        return await handler(event, data)
