import weaviate
import weaviate.classes as wvc
from weaviate.auth import AuthApiKey
import os
import requests
import json
import ijson
import wget
import logging

def semantic_search(query='computers', limit=2) -> dict:
    print(f'\nSemantic Search, query = {query}.')
    print(f'limit = {limit}')
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
    try:

        weaviate_host = os.getenv("WEAVIATE_HOST")        # Recommended: save to an environment variable
        # weaviate_host = "weaviate"
        weaviate_key = os.getenv("WEAVIATE_API_KEY")    # Recommended: save to an environment variable

        logging.basicConfig(level=logging.INFO)
        client = weaviate.connect_to_custom(
            http_host=weaviate_host,
            auth_credentials=AuthApiKey(weaviate_key),
            http_port=80,
            http_secure=False,
            grpc_host="weaviate-grpc.weaviate",
            grpc_port=50051,
            grpc_secure=False,
            skip_init_checks=False,
            headers={"X-OpenAI-Api-key": os.getenv("OPENAI_API_KEY")}
        )

        symbols = client.collections.get("Symbols")
        print(f'symbols: {symbols}')

        if client.is_ready():
            logging.info('')
            logging.info(f'Found {len(client.cluster.nodes())} Weaviate nodes.')
            logging.info('')
            for node in client.cluster.nodes():
                logging.info(node)
                logging.info('')
            print(semantic_search())

    finally:
        client.close()  # Close client gracefully

