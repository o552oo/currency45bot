import requests
from config import keys


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обраотать количество {amount}')

        url = "https://api.fastforex.io/convert"
        querystring = {"from": f"{quote_ticker}", "to": f"{base_ticker}", "amount": f"{amount}", "api_key": "561e2e31d8-02e106f180-qz5mu3"}
        headers = {"Accept": "application/json"}

        total_base = requests.request("GET", url, headers=headers, params=querystring)
        return total_base.text
