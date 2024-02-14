import weaviate_utils
import os
import logging
import requests
import json
import gradio as gr

client = weaviate_utils.weaviate_connection()
logging.info(f'\nclient.is_ready() = {client.is_ready()}')

LIMIT = 5

# weaviate_utils.import_questions(client)

#
# OpenAI query
#
def generative_search(concept: str, prompt: str) -> str:
    response = (
        client.query
        .get("Article", ["title", "text"])
        .with_near_text({"concepts": [concept]})
        .with_generate(single_prompt=prompt)
        .with_limit(1)
        .do()
    )

    logging.info('==> OpenAI query')
    logging.info(json.dumps(response, indent=4))
    output = json.dumps(response, indent=4)
    result = response.get('data')['Get']['Article'][0]['_additional']['generate']['singleResult']
    return result

def semantic_search(query: str, limit: int = 3):
    nearText = {
        "concepts": [query], # example from earlier -> 'kitten'
        # "distance": -139.0,
    }

    properties = [
        "text", "title", "url", "views",
        "_additional {distance}"
    ]

    response = (
        client.query
        .get("Article", properties)
        .with_near_text(nearText)
        .with_limit(limit)
        .do()
    )

    result = ""
    for i in range(limit):
        result = result + response['data']['Get']['Article'][i]['title'] + ": " + response['data']['Get']['Article'][i]['text']
        result += '\n\n'

    return result
#
# Gradio interface
#
with gr.Blocks() as demo:
    semantic_examples = [
        ["famous criminals", "Summarize the {text}" ],
        ["famous bank robberies", "Summarize the {text}"]
    ]
    semantic_input_text = gr.Textbox(label="concept", value=semantic_examples[0][0])
    vdb_button = gr.Button(value="Search the Wikipedia vector DB")
    vdb_button.click(fn=semantic_search, inputs=semantic_input_text, outputs=gr.Textbox(label="Search Results"))
    gr.Examples(semantic_examples,
        fn=semantic_search,
        inputs=semantic_input_text
        )

    button = gr.Button(value="Perform a Generative Search")
    
    examples=[
        ["famous criminals", "Based on the {text}, write five questions to interview a panel of jurors in a criminal court. ."],
        ["famous bank robberies", "Summarize the chances of convicting a person for the crime explained in the {text} as you might to a panel of jurors in a criminal court.  Limit the answer to two paragraphs."],
    ]

    generative_search_input_text = gr.Textbox(label="concept", value=examples[0][0])
    generative_search_prompt_text = gr.Textbox(label="prompt", value=examples[0][1])
    button.click(fn=generative_search,
    inputs=[generative_search_input_text, generative_search_prompt_text],
    outputs=gr.Textbox(label="Generative Search Results"))
    gr.Examples(examples,
        fn=generative_search,
        inputs=[generative_search_input_text, generative_search_prompt_text]
    )
    
demo.queue(max_size=10)
demo.launch(server_name='0.0.0.0', server_port=8080)

