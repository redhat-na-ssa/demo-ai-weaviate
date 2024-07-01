# https://www.alphavantage.co/query?function=OVERVIEW&symbol=BC/PA&apikey=MY_API_KEY
import requests
import pandas as pd
import json
import time
import os
import urllib
from urllib.parse import urlparse

def retrieve_data(function: str, symbol: str, api_key: str) -> dict:
    """
    Retrieves data from AlphaVantage's open API.
    Documentation located at: https://www.alphavantage.co/documentation
    """
    # query from API
    encoded_symbol = urllib.parse.quote(symbol, safe='')
    url = f'https://www.alphavantage.co/query?function={function}&symbol={encoded_symbol}&apikey={api_key}'
    response = requests.get(url)
    # read output
    data = response.text
    # parse output
    parsed = json.loads(data)

    return parsed


if __name__ == '__main__':

    api_key = os.environ.get('ALPHA_VANTAGE_API_KEY') 
    ticker = 'BC/PA'
    # ticker= 'HPE'
    d = retrieve_data('OVERVIEW', ticker, api_key)
    print(d)