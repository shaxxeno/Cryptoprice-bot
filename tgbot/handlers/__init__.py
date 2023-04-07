from aiogram import Router

from . import basic
from . import user

router = Router(name='handlers_router')

router.include_routers(
    basic.router,
    user.router
)
