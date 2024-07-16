import weaviate
import weaviate.classes as wvc
from weaviate.auth import AuthApiKey
import os
import requests
import json
import ijson
import wget
import logging

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
        headers={"X-OpenAI-Api-key": os.getenv("OPENAI_API_KEY"),
                 "X-Huggingface-Api-key": os.getenv("HUGGINGFACE_API_KEY")}
        )

        symbols = client.collections.get("Symbols")
        logging.debug(f'symbols: {symbols}')
        logging.info(semantic_search(symbols))
    except:
        logging.error('Connection to Weaviate failed!')
        quit(1)


    client.close()  

