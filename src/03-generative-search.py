import weaviate_utils
import logging
import json

client = weaviate_utils.weaviate_connection()
logging.info(f'\nclient.is_ready() = {client.is_ready()}')

#
# OpenAI query
#

# instruction for the generative module
response = (
    client.query
    .get("Question", ["question", "answer", "category"])
    .with_near_text({"concepts": ["biology"]})
    .with_generate(single_prompt="Explain {answer} as you might to a five-year-old.")
    .with_limit(2)
    .do()
)

logging.info('==> OpenAI query')
logging.info(json.dumps(response, indent=4))

