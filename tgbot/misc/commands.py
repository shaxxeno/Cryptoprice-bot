from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Start bot'
        ),
        BotCommand(
            command='p',
            description='Price of coin(eg. /p btc, /p eth)'
        ),
        BotCommand(
            command='listings',
            description='Top 10 coins by CoinMarketCap'
        ),
        BotCommand(
            command='gainers',
            description='Best performing coins by CoinMarketCap'
        ),
        BotCommand(
            command='losers',
            description='Worst performing coins by CoinMarketCap'
        ),
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())
