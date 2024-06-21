import weaviate
from weaviate.auth import AuthApiKey
import logging
import os
if __name__ == '__main__':

    weaviate_host = os.getenv("WEAVIATE_HOST")     
    weaviate_key = os.getenv("WEAVIATE_API_KEY")

    logging.basicConfig(level=logging.INFO)
    client = weaviate.connect_to_custom(
        http_host=weaviate_host,
        auth_credentials=AuthApiKey(weaviate_key),
        http_port=80,
        http_secure=False,
        grpc_host="weaviate-grpc.weaviate",
        grpc_port=50051,
        grpc_secure=False,
        skip_init_checks=False
    )

    if client.is_ready():
        logging.info('')
        logging.info(f'Found {len(client.cluster.nodes())} Weaviate nodes.')
        logging.info('')
        for node in client.cluster.nodes():
            logging.info(node)
            logging.info('')
