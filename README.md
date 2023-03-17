# Cryptocurrency Price Bot

<p>This bot displays the current price of various cryptocurrencies. 
You can use this bot to stay up-to-date on the latest price 
movements of popular cryptocurrencies like Bitcoin, 
Ethereum, Litecoin, and many others.
</p>

![Example image](src/img.png)

## Installation
<p>To install and use this bot, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running:

```pip install -r requirements.txt```

3. Create a .env file in the project root directory, copy all variables from .env.sample and fill the required fields:
</p>

```
BOT_TOKEN= <your-bot_token>
CMC_API_KEY= <your-api-key>
ADMINS= <admin-ids>
```
Note: You can obtain an API key by signing up for a CoinMarketCap API.


Run the bot by running 
```python bot.py```

## Usage

Once the bot is running, you can use following commands:
```
/start - start the bot
/p - coin's price (eg. /p btc)
/listings - top 10 coins by CoinMarketCap
/gainers - best performing coins
/losers - worst performing coins
```

## Contributing
If you would like to contribute to this project, feel free to fork 
the repository and submit a pull request. Any contributions are welcome, 
whether it's adding new features, fixing bugs, or improving the documentation.

## License

This project is licensed under the MIT License - see the LICENSE file for details.