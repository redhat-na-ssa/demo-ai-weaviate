import weaviate_utils
import os
import logging
import requests
import json
import gradio as gr

client = weaviate_utils.weaviate_connection()
logging.info(f'\nclient.is_ready() = {client.is_ready()}')

weaviate_utils.import_questions(client)

#
# OpenAI query
#
def generative_search(concept: str, prompt: str) -> str:
    response = (
        client.query
        .get("Question", ["question", "answer", "category"])
        .with_near_text({"concepts": [concept]})
        .with_generate(single_prompt=prompt)
        .with_limit(1)
        .do()
    )

    logging.info('==> OpenAI query')
    logging.info(json.dumps(response, indent=4))
    output = json.dumps(response, indent=4)
    result = response.get('data')['Get']['Question'][0]['_additional']['generate']['singleResult']
    return result
gr.Interface(max_lines=50, fn=generative_search, inputs=["text", "text"], outputs="text",
    examples=[["biology", "Explain {answer} as you might to a five-year-old."],
              ["biology", "Explain {answer} as you might to a graduate student."],
              ["biology", "Explain {answer} as lyrics for a rap tune. Limit the answer to a single verse and chorus."]])\
    .queue().launch(server_name='0.0.0.0', server_port=8080)