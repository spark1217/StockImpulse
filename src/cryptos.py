"""
This file is responsible for any requests related to crypto currency.
"""

import requests

def get_crypto_info(crypto_name):
    """
    This method is responsible for getting the information for one crypto token and returning
    the JSON response.
    """
    key = "https://api.binance.com/api/v3/ticker/price?symbol=" + crypto_name + "USDT"
    data = requests.get(key, timeout=10)
    if int(data.status_code / 100) == 4:
        raise NameError(f'There was an issue getting the information for {crypto_name}.')
    data = data.json()
    return data
    