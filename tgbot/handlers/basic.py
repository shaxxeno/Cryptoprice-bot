from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name='basic')


@router.message(Command(commands=['start']))
async def user_start(message: Message):
    await message.answer(f'Hi, {message.from_user.first_name}!'
                         f'\nTo check the cryptocurrency just write it down(i.e. /p btc, /p eth)')
