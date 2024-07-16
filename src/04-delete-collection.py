import weaviate
import weaviate.classes as wvc
from weaviate.auth import AuthApiKey
import os
import requests
import json
import ijson
import wget
import logging


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:

        # ollama_api_endpoint = os.getenv("OLLAMA_HOST", "http://ollama-svc.ollama")
        # ollama_vectorizer_model = model = os.getenv("OLLAMA_VECTORIZER", "all-minilm")
        # ollama_generative_model = os.getenv("OLLAMA_LLM","llama3:8b-instruct-q8_0")
        weaviate_host = os.getenv("WEAVIATE_HOST", "weaviate.weaviate")
        weaviate_key = os.getenv("WEAVIATE_API_KEY")

        logging.basicConfig(level=logging.INFO)

        if weaviate_key == None:
            logging.error('')
            logging.error('WEAVIATE_API_KEY not set!')
            logging.error('Please set WEAVIATE_API_KEY environment variable.')
            logging.error('')
            
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

        logging.info('\nDeleting the Symbols collection\n')
        client.collections.delete("Symbols")

    finally:
        client.close()

