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

    # Convert and write JSON object to file
    # with open("data/symbols/" + symbol + ".json", "w") as outfile: 
    #     json.dump(parsed, outfile)
    #     print(f'Saved {outfile}')

    print(f'Retrieved {symbol}, response = {response.status_code} ')
    return parsed

#
# This should be a function
#
# Convert and write the python dict object to file.
#
# Input:
#   dictionary: dict
#   filename: str
#
# Output:
#   bool (True if successful, False otherwise)
#
# Example:
#   dict_to_json_file(dictionary=company_overview, filename='IBM.json') -> True or False 
#
def dict_to_json_file(dictionary: dict, filename: str) -> bool:
    with open(filename, "w") as outfile: 
        json.dump(list_of_symbols, outfile)
        print(f'Saved {outfile}')
    return True

# company_overview = retrieve_data('OVERVIEW', 'IBM', 'None')

# tickers = ['IBM', 'MSFT', 'AMZN', 'GOOG', 'AAPL', 'NFLX', 'NVDA', 'TSLA', 'PYPL', 'BABA', 'ADBE', 'AMD', 'INTC', 'CSCO', 
#            'NKE', 'JNJ', 'PEP', 'WMT', 'COST', 'KO', 'JPM', 'DIS']

#
# Retreive a list of symbols from the CSV file
#
 
df = pd.read_csv('data/tickers.csv')

#
# Retreive an overview for each symbol and save the data to a JSON file in the data directory.
# 
# list_of_symbols = []

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



# print(list_of_symbols)

#
# Save all of the data to a single JSON file in the data directory.
# 
# dict_to_json_file('list_of_symbols', 'data/output.json')
