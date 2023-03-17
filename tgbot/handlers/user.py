from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from tgbot.config import load_config
from tgbot.classes.cmc_data import Price, Listings, GainersLosers

user_router = Router()


@user_router.message(Command(commands=['start']))
async def user_start(message: Message):
    await message.answer(f'Hi, {message.from_user.first_name}!'
                         f'\nTo check the cryptocurrency just write it down(i.e. /p btc, /p eth)')


@user_router.message(Command(commands=['p']))
async def cmc_price(message: Message, command: CommandObject):
    if command.args:
        try:
            price_data = Price(load_config().cmc.url_quotes,
                               load_config().cmc.cmc_api)
            await price_data.get_cmc_data(command.args.upper())
            price = price_data.get_price()
            await message.answer(price)
        except IndexError:
            await message.answer('Check if the coin spelling is correct')
    else:
        await message.answer('Use this command to get the price of the coin (eg. /p btc, /p eth)')


@user_router.message(Command(commands=['listings']))
async def cmc_listing(message: Message):
    listings_data = Listings(load_config().cmc.url_listings,
                             load_config().cmc.cmc_api)
    await listings_data.get_cmc_data()
    listings = listings_data.get_listings()
    await message.answer(f'<b>Top 10 by Market Cap \u26a1\ufe0f</b>'
                         f'\n\n{listings}')


@user_router.message(Command(commands='gainers'))
async def gainers_losers(message: Message):
    gainers = GainersLosers(load_config().cmc.url_performing, 0)
    await message.answer(f'<b>Top 10 gainers by Market Cap</b> \U0001f4c8'
                         f'\n\n{await gainers.get_data()}')


@user_router.message(Command(commands='losers'))
async def gainers_losers(message: Message):
    losers = GainersLosers(load_config().cmc.url_performing, 1)
    await message.answer(f'<b>Top 10 losers by Market Cap</b> \U0001f4c9'
                         f'\n\n{await losers.get_data()}')
