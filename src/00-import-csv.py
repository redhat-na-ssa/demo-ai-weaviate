import weaviate
import weaviate.classes as wvc
from weaviate.auth import AuthApiKey
import os
import requests
import json
import ijson
import wget
import logging

def download_data():
    print("Downloading symbols...") 
    url = "https://koz-data.s3.us-east-2.amazonaws.com/symbols.json"
    wget.download(url, "data/symbols.json")


def ingest_data(client):

    # ===== Define the collection =====
    symbols = client.collections.create(
        name="Symbols",
        vectorizer_config=wvc.config.Configure.Vectorizer.text2vec_openai(),  # If set to "none" you must always provide vectors yourself. Could be any other "text2vec-*" also.
        generative_config=wvc.config.Configure.Generative.openai()  # Ensure the `generative-openai` module is used for generative queries
    )

    # Settings for displaying the import progress
    counter = 0
    interval = 100  # print progress every this many records; should be bigger than the batch_size

    print("JSON streaming, to avoid running out of memory on large files...")
    with client.batch.fixed_size(batch_size=50) as batch:
        with open("data/symbols.json", "rb") as f:
            objects = ijson.items(f, "item")
            for obj in objects:
                properties = {
                    "Symbol": obj["Symbol"],
                    "Name": obj["Name"],
                    "Description": obj["Description"],
                    "CIK": obj["CIK"],
                    "Exchange": obj["Exchange"],
                    "Currency": obj["Currency"],
                    "Country": obj["Country"],
                    "Sector": obj["Sector"], 
                    "Industry": obj["Industry"],
                    "Address": obj["Address"],
                    "FiscalYearEnd": obj["FiscalYearEnd"],
                    "LatestQuarter": obj["LatestQuarter"],
                    "MarketCapitalization": obj["MarketCapitalization"],
                    "BookValue": obj["BookValue"],
                    "EBITDA": obj["EBITDA"],
                    "PERatio": obj["PERatio"],
                    "PEGRatio": obj["PEGRatio"],
                    "DividendPerShare": obj["DividendPerShare"],
                    "DividendYield": obj["DividendYield"],
                    "EPS": obj["EPS"],
                    "RevenuePerShareTTM": obj["RevenuePerShareTTM"],
                    "ProfitMargin": obj["ProfitMargin"],
                    "OperatingMarginTTM": obj["OperatingMarginTTM"],
                    "ReturnOnAssetsTTM": obj["ReturnOnAssetsTTM"],
                    "ReturnOnEquityTTM": obj["ReturnOnEquityTTM"],
                    "RevenueTTM": obj["RevenueTTM"],
                    "GrossProfitTTM": obj["GrossProfitTTM"],
                    "DilutedEPSTTM": obj["DilutedEPSTTM"],
                    "QuarterlyEarningsGrowthYOY": obj["QuarterlyEarningsGrowthYOY"],
                    "QuarterlyRevenueGrowthYOY": obj["QuarterlyRevenueGrowthYOY"],
                    "AnalystTargetPrice": obj["AnalystTargetPrice"],
                    "AnalystRatingStrongBuy": obj["AnalystRatingStrongBuy"],
                    "AnalystRatingBuy": obj["AnalystRatingBuy"],
                    "AnalystRatingHold": obj["AnalystRatingHold"],
                    "AnalystRatingSell": obj["AnalystRatingSell"],
                    "AnalystRatingStrongSell": obj["AnalystRatingStrongSell"],
                    "TrailingPE": obj["TrailingPE"],
                    "ForwardPE": obj["ForwardPE"],
                    "PriceToSalesRatioTTM": obj["PriceToSalesRatioTTM"],
                    "PriceToBookRatio": obj["PriceToBookRatio"],
                    "EVToRevenue": obj["EVToRevenue"],
                    "EVToEBITDA": obj["EVToEBITDA"],
                    "Beta": obj["Beta"],
                    "fiftytwoWeekHigh": obj["52WeekHigh"],
                    "fiftytwoWeekLow": obj["52WeekLow"],
                    "fiftyDayMovingAverage": obj["50DayMovingAverage"],
                    "twohundredDayMovingAverage": obj["200DayMovingAverage"],
                    "SharesOutstanding": obj["SharesOutstanding"],
                    "DividendDate": obj["DividendDate"],
                    "ExDividendDate": obj["ExDividendDate"]
                }
                batch.add_object(
                    collection="Symbols",
                    properties=properties,
                    # If you Bring Your Own Vectors, add the `vector` parameter here
                    # vector=obj.vector["default"]
                )

                # Calculate and display progress
                counter += 1
                if counter % interval == 0:
                    print(f"Imported {counter} symbols.")


    print(f"Finished importing {counter} symbols.")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        download_data()

        weaviate_url = os.getenv("WEAVIATE_URL")        # Recommended: save to an environment variable
        # weaviate_url = "weaviate"
        weaviate_key = os.getenv("WEAVIATE_API_KEY")    # Recommended: save to an environment variable

        logging.basicConfig(level=logging.INFO)
        client = weaviate.connect_to_custom(
            http_host=weaviate_url,
            auth_credentials=AuthApiKey(weaviate_key),
            http_port=80,
            http_secure=False,
            grpc_host="weaviate-grpc.weaviate",
            grpc_port=50051,
            grpc_secure=False,
            skip_init_checks=False,
            headers={"X-OpenAI-Api-key": os.getenv("OPENAI_API_KEY")}
        )

        client.collections.delete("Symbols")

        print('\nIngesting data\n')
        ingest_data(client)

        symbols = client.collections.get("Symbols")
        print(f'symbols: {symbols}')

        if client.is_ready():
            logging.info('')
            logging.info(f'Found {len(client.cluster.nodes())} Weaviate nodes.')
            logging.info('')
            for node in client.cluster.nodes():
                logging.info(node)
                logging.info('')
    finally:
        client.close()  # Close client gracefully

