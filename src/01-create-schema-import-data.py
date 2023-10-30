import weaviate_utils
import os
import logging
import requests
import json

logging.basicConfig(level=logging.INFO)

client = weaviate_utils.weaviate_connection()
logging.info('\nclient.isReady(): %s', client.is_ready())
logging.info('cluster.get_nodes_status(): %s', client.cluster.get_nodes_status())

class_obj = {
    "class": "Question",
    "vectorizer": "text2vec-huggingface",
    "moduleConfig": {
        "text2vec-huggingface": {},
        "model": "sentence-transformers/all-MiniLM-L6-v2",
        # Ensure the `generative-openai` module is used for generative queries
        "generative-openai": {
          "model": "gpt-3.5-turbo",  # Optional - Defaults to `gpt-3.5-turbo`
        }
    }
}

#
# Create the class if its not there
#

if client.schema.exists('Question'):
    logging.info("Question class already exists, skipping class creation.")
else:
    logging.info(f'\nCreating the Question class using the text2vec-huggingface vectorizer.')
    client.schema.create_class(class_obj)


#
# Load some questions.
#
resp = requests.get(
    'https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json')
data = json.loads(resp.text)  # Load data

client.batch.configure(batch_size=100)  # Configure batch
with client.batch as batch:  # Initialize a batch process
    for i, d in enumerate(data):  # Batch import data
        print(f"importing question: {i+1}")
        properties = {
            "answer": d["Answer"],
            "question": d["Question"],
            "category": d["Category"],
        }
        batch.add_data_object(
            data_object=properties,
            class_name="Question"
        )