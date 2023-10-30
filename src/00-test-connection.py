import weaviate_utils
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    client = weaviate_utils.weaviate_connection()

    if client.is_ready():
        logging.info('')
        logging.info(f'Found {len(client.cluster.get_nodes_status())} Weaviate nodes.')
        logging.info('')
        for node in client.cluster.get_nodes_status():
            logging.info(node)
            logging.info('')
