import requests

bot_url = 'https://t.me/TestTopTest_bot'
token = '5650326437:AAH0rMs2bfm4cSNbFqj-Lwzel0FahHZ5b4g'
currencies = ['USD', 'RUB', 'JPY', 'EUR', 'BTC', 'ETH']


class Requests:
    @staticmethod
    def get_price(base, quote, amount):
        url = 'https://min-api.cryptocompare.com/data/price'

        parameters = {'fsym': base,
                      'tsyms': quote}

        response = requests.get(url, params=parameters)
        data = response.json()[quote] * amount

        return data
