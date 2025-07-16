import weaviate
import weaviate.classes as wvc
from weaviate.auth import AuthApiKey
import os
import requests
import json
import ijson
import wget
import logging

def generative_search(symbols, query='computers', task=None, limit=2) -> str:
    print(f'\nPerforming generative search, query = {query}, limit = {limit}.')
    print(f'Prompt: {task}')
    print(f'limit = {limit}')
    response = symbols.generate.near_text(
        query=query,
        limit=limit,
        grouped_task=task
    )

    print(f'response = {response.generated}')

    return response.generated

def semantic_search(symbols, query='computers', limit=2) -> dict:
    logging.info(f'\nSemantic Search, query = {query}.')
    logging.info(f'limit = {limit}')
    response = symbols.query.near_text(
        query=query,
        limit=limit
    )

    return_list = []
    for i in range(limit):
        return_list.append(response.objects[i].properties['name'])
    return return_list

if __name__ == '__main__':
    
    logging.basicConfig(level=logging.INFO)

    weaviate_host = os.getenv("WEAVIATE_HOST", "weaviate.weaviate") 
    logging.info(f'WEAVIATE_HOST = {weaviate_host}')

    weaviate_key = os.getenv("WEAVIATE_API_KEY")

    if weaviate_key == None:
        logging.error('WEAVIATE_API_KEY not set!')
        quit(1)

    logging.basicConfig(level=logging.INFO)

    try:
        client = weaviate.connect_to_custom(
        http_host=weaviate_host,
        auth_credentials=AuthApiKey(weaviate_key),
        http_port=80,
        http_secure=False,
        grpc_host="weaviate-grpc.weaviate",
        grpc_port=50051,
        grpc_secure=False,
        skip_init_checks=True,
        # additional_config=AdditionalConfig(
        #     timeout=Timeout(init=30, query=60, insert=120)  # Values in seconds
        #     )
    )

        symbols = client.collections.get("Symbols")
        logging.debug(f'symbols: {symbols}')

        query = "computers"
        limit = 1
        logging.info(semantic_search(symbols, query = query, limit = limit))
        logging.info(generative_search(symbols, query = query, task = "Summarize the information from a financial investment perspective", limit = limit))
    except:
        logging.error('Connection to Weaviate failed!')
        quit(1)


    client.close()  

