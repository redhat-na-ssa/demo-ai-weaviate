### Download data to `data/wiki_simple_100k.parquet`

# Link: [google drive](https://drive.google.com/file/d/1_sBvE9RKYUSHGSfJomiLf-2d7O6SUIoS/view)

## ☁️☁️ Configure the Weaviate Cloud Instance ☁️☁️
### Free 14 day sandbox here: https://console.weaviate.cloud/

import os
import weaviate
import json
import weaviate_utils
import os
import logging
import requests

logging.basicConfig(level=logging.INFO)

client = weaviate_utils.weaviate_connection()
logging.info('\nclient.isReady(): %s', client.is_ready())
logging.info('cluster.get_nodes_status(): %s', client.cluster.get_nodes_status())


"""## ䷀䷀Create Database Schema䷀䷀"""

# delete existing schema, (note, this will delete all your weaviate data)
# run this if you are re-creating from the beginning
client.schema.delete_all()

