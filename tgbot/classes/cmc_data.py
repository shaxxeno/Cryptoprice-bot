import aiohttp
from bs4 import BeautifulSoup


class CoinMarketCapParams:
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key


class Price(CoinMarketCapParams):

    async def get_cmc_data(self, symbol):
        self.symbol = symbol
        url = self.url
        headers = {
            'X-CMC_PRO_API_KEY': self.api_key,
        }
        parameters = {
            'symbol': self.symbol,
            'convert': 'USD'
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=headers, params=parameters) as response:
                self.response_data = await response.json()

    def get_price(self):
        response_quote = self.response_data['data'][self.symbol][0]['quote']['USD']
        slug = self.response_data['data'][self.symbol][0]['slug']
        price = round(response_quote['price'])
        market_cap = round(response_quote['market_cap'])
        volume_24h = round(response_quote['volume_24h'])
        percent_change_1h = response_quote['percent_change_1h']
        percent_change_24h = response_quote['percent_change_24h']
        percent_change_7d = response_quote['percent_change_7d']
        chart_link = f"<a href='https://coinmarketcap.com/currencies/{slug}/'>Charts</a>"
        text = f'\U0001F4B8Price: {price:,.2f}$' \
               f'\n\U0001f4b0Market Cap: {market_cap:,}$' \
               f'\n\U0001f4b1Volume 24H: {volume_24h:,}$' \
               f'\n\U0001f4c8Percent Change 1H: {percent_change_1h:.2f}%' \
               f'\n\U0001f4c8Percent Change 24H: {percent_change_24h:.2f}%' \
               f'\n\U0001f4c8Percent Change 7d: {percent_change_7d:.2f}%' \
               f'\n{"-" * 20}' \
               f'\n\U0001f4b9{chart_link}|Coinmarketcap'
        return text


class Listings(CoinMarketCapParams):

    async def get_cmc_data(self):
        url = self.url
        headers = {
            'X-CMC_PRO_API_KEY': self.api_key,
        }
        params = {
            'limit': 10,
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=headers, params=params) as response:
                self.response_data = await response.json()

    def get_listings(self):
        response_listings = self.response_data['data']
        result = []
        for index, coin in enumerate(response_listings, start=1):
            name = coin['symbol']
            price = coin['quote']['USD']['price']
            percent_change_24h = coin['quote']['USD']['percent_change_24h']
            text = f'{index}. {name}: {price:,.2f}$ | {percent_change_24h:.2f}%'
            result.append(text)
        text = '\n'.join(result)
        return text


class GainersLosers:
    def __init__(self, url, index):
        self.url = url
        self.index = index

    async def get_data(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                soup = BeautifulSoup(await response.text(), 'html.parser')

        data_table = soup.find_all('table')[self.index]
        data_rows = data_table.find_all('tr')[1:]
        result = []
        for index, row in enumerate(data_rows[:10], start=1):
            name = row.find_all('td')[1].find('p', class_='sc-e225a64a-0 dfeAJi coin-item-symbol').text
            price = float(row.find_all('td')[2].text.replace('$', '').replace(',', ''))
            percent_change = float(row.find_all('td')[3].text.replace('%', '').replace(',', ''))
            text = f'{index}. {name}: {price:,.2f}$ | {percent_change:.2f}%'
            result.append(text)
        text = '\n'.join(result)
        return text

