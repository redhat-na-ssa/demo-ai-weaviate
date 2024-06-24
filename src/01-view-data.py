import os
import requests
import json
import ijson
import wget
import logging
import pandas as pd

def download_data():
    try:
      os.stat("data/symbols.json")
      logging.info("Symbols already downloaded")
    except:
      logging.info("Downloading symbols...")
      url = "https://koz-data.s3.us-east-2.amazonaws.com/symbols.json"
      wget.download(url, "data/symbols.json")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
   
    download_data()
    try:
        df = pd.read_json("data/symbols.json")
        logging.info(df.head())
    except:
        logging.error("Error loading symbols!")