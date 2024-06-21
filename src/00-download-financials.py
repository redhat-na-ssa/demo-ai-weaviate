#
# This script will download financial overviews from AlphaVantage.
# It is expected to take 3-4 hours since I'm using the most
# cost effective subscription plan (75 api calls/minute). A
# download.json file will get created and populated with overview
# data including some nulls {}, and Errors. The nulls and errors
# must be removed and at this time I'm using a manual process shown below.
#
# Remove the lines that begin with {},
#
# sed '/^{},$/d' output.json > tmp1.json
#
# Remove the lines that contain Error
# sed '/Error/d' tmp1.json > tmp2.json
# mv tmp2.json symbols.json
#

import requests
import pandas as pd
import json
import time
import os

#
# AlphaVantage API key 
#
api_key = os.environ.get('ALPHA_VANTAGE_API_KEY') 

#
# Grab the list of tickers from AlphaVantage
#
 
url = "https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=demo"
df = pd.read_csv(url)

df.to_csv('data/tickers.csv', header=True)

def pretty_print(data: dict):
    print(json.dumps(data, indent=4))

def retrieve_data(function: str, symbol: str, api_key: str) -> dict:
    """
    Retrieves data from AlphaVantage's open API.
    Documentation located at: https://www.alphavantage.co/documentation
    """
    # query from API
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    # read output
    data = response.text
    # parse output
    parsed = json.loads(data)

    return parsed

def retrieve_data_to_csv(function: str, symbol: str, api_key: str) -> dict:
    """
    Retrieves data from AlphaVantage's open API.
    Documentation located at: https://www.alphavantage.co/documentation
    """
    # query from API
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}'
    

    response = requests.get(url)
    # read output
    data = response.text
    # parse output
    parsed = json.loads(data)

    print(f'Retrieved {symbol}, response = {response.status_code} ')
    return parsed

#
# Convert and return the python dict object.
#

def dict_to_json_file(dictionary: dict, filename: str) -> bool:
    with open(filename, "w") as outfile: 
        json.dump(list_of_symbols, outfile)
        print(f'Saved {outfile}')
    return True

#
# Retreive a list of symbols from the CSV file
#
 
df = pd.read_csv('data/tickers.csv')

#
# Retreive an overview for each symbol and save the data to a JSON file in the data directory.
# A total hack.

filename="data/output.json"
os.remove(filename)
 
with open(filename, "a") as outfile: 
    outfile.write("[\n")
    for ticker in df.iloc[:]['symbol']:
        json.dump(retrieve_data_to_csv('OVERVIEW', ticker, api_key), outfile)
        outfile.write(',\n')
        time.sleep(1)

    outfile.write("]")

    outfile.close()
    print(f'Saved {outfile}')

