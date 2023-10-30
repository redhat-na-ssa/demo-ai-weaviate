import weaviate_utils
import os
import logging
import requests
import json

client = weaviate_utils.weaviate_connection()
logging.info(f'\nclient.is_ready() = {client.is_ready()}')

#
# Queries
#
result = client.query.get("Question", ["question", "answer"]).with_additional(
    ["score"]).with_hybrid("Venus", alpha=0.25, properties=["question"]).with_limit(3).do()

print(json.dumps(result, indent=4))

response = (
    client.query
    .get("Question", ["question", "answer", "category"])
    .with_near_text({"concepts": ["biology"]})
    .with_where({
        "path": ["category"],
        "operator": "Equal",
        "valueText": "ANIMALS"
    })
    .with_limit(2)
    .do()
)

print(json.dumps(response, indent=4))

response = (
    client.query
    .get("Question", ["question", "answer", "category"])
    .with_near_text({"concepts": ["biology"]})
    .with_limit(2)
    .do()
)

print(json.dumps(response, indent=4))

# print(f'\nDeleting the Question class...\n')
# client.schema.delete_class('Question')
