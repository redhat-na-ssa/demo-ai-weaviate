import weaviate_utils
import os
import logging
import requests
import json
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

client = weaviate_utils.weaviate_connection()
logging.info('\nclient.isReady(): %s', client.is_ready())
logging.info('cluster.get_nodes_status(): %s', client.cluster.get_nodes_status())
logging.info('Deleting the Question class...')
client.schema.delete_class('Question')
