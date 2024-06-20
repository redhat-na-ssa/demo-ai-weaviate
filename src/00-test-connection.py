# import weaviate_utils
import weaviate
from weaviate.auth import AuthApiKey
import logging
import os
if __name__ == '__main__':

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
        skip_init_checks=False
    )


    # client = weaviate.connect_to_weaviate_cloud(
    #     cluster_url=os.getenv("WCD_DEMO_URL"),  # Replace with your Weaviate Cloud URL
    #     auth_credentials=weaviate.auth.AuthApiKey(os.getenv("WCD_DEMO_RO_KEY")),  # Replace with your Weaviate Cloud key
    #     headers={'X-OpenAI-Api-key': os.getenv("OPENAI_API_KEY")}  # Replace with your OpenAI API key
    # )

    if client.is_ready():
        logging.info('')
        logging.info(f'Found {len(client.cluster.nodes())} Weaviate nodes.')
        logging.info('')
        for node in client.cluster.nodes():
            logging.info(node)
            logging.info('')
