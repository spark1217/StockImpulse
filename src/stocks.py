"""
This file is responsible for handling stock requests from the FinnHub API and
handling any errors that occur when making these requests.
"""

import finnhub
import config

FINNHUB_TOKEN = config.tokens['finnhub_token']
"""FinnHub API Token"""


def setup_finnhub():
    """
    This method makes sure the finnhub_client is setup before trying to use finnhub
    """
    return finnhub.Client(api_key=FINNHUB_TOKEN)

def get_stock_info(stock_name):
    """
    This function gets and returns the information for a stock from the FinnHub API.
    """
    finnhub_client = setup_finnhub()
    stock_info = finnhub_client.quote(stock_name.upper())
    if all((v == 0) or (v is None) for v in stock_info.values()):
        raise NameError(f'```Stock {stock_name} does not exist or has no value.```')
    return stock_info
