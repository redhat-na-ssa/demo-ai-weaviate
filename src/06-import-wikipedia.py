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

article_schema = {
    "class": "Article",
    "description": "Wiki Article",
    # "vectorizer": "text2vec-huggingface",
    # "moduleConfig": {
        # "text2vec-huggingface": {},
        # "model": "sentence-transformers/all-MiniLM-L6-v2",
    "vectorizer": "text2vec-cohere",#multi-lingual
    "moduleConfig": {
        "text2vec-cohere": {
            "model": "multilingual-22-12",
            "truncate": "RIGHT"
       },
        "generative-openai":{"model": "gpt-3.5-turbo"},
    },
    "vectorIndexConfig": {
        "distance": "dot"
    },
    "properties": [
    {
        "name": "text",
        "dataType": [ "text" ],
        "description": "Article body",
        "moduleConfig": {
            "text2vec-cohere": {
                "skip": False,
                "vectorizePropertyName": False
            }
        }
    },
    {
        "name": "title",
        "dataType": [ "string" ],
        "moduleConfig": { "text2vec-cohere": { "skip": True } }
    },
    {
        "name": "url",
        "dataType": [ "string" ],
        "moduleConfig": { "text2vec-cohere": { "skip": True } }
    },
    {
        "name": "wiki_id",
        "dataType": [ "int" ],
        "moduleConfig": { "text2vec-cohere": { "skip": True } }
    },
    {
        "name": "views",
        "dataType": [ "number" ],
        "moduleConfig": { "text2vec-cohere": { "skip": True } }
    },
    ]
}

# add the schema
#client.schema.delete_all()
client.schema.create_class(article_schema)

print("The schema has been created")

import pandas as pd
df = pd.read_parquet('data/wiki_simple_100k.parquet')

df['emb'][0].shape[0]

df.head()

"""## 💽💽 Batch and Add 100k Wikipedia Articles to Weaviate 💽💽"""

### Step 1 - configure Weaviate Batch, which optimizes CRUD operations in bulk
# - starting batch size of 100
# - dynamically increase/decrease based on performance
# - add timeout retries if something goes wrong

client.batch.configure(
    batch_size=200,
    dynamic=True,
    timeout_retries=3,
)

data = df[:100000] # make sure it is not more than 100k objects

counter=0

with client.batch as batch:
    for idx, item in data.iterrows():
        # print update message every 100 objects
        if (counter %100 == 0):
            print(f"Import {counter} / {len(data)} ", end="\r")

        properties = {
        "text": item["text"],
        "title": item["title"],
        "url": item["url"],
        "views": item["views"],
        "wiki_id": item["wiki_id"]
        }

        vector = item["emb"]

        batch.add_data_object(properties, "Article", None, vector)
        counter = counter+1
    print(f"Import {counter} / {len(data)}")

print("Import complete")

# Test that all data has loaded – get object count
result = (
    client.query.aggregate("Article")
    .with_fields("meta { count }")
    .do()
)
print("Object count: ", result["data"]["Aggregate"]["Article"])

