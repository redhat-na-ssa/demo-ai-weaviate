import weaviate
import weaviate.classes as wvc
from weaviate.auth import AuthApiKey
from weaviate.classes.init import AdditionalConfig, Timeout
import os
import requests
import json
import ijson
import gradio as gr
import logging

def connect_weaviate_custom():
    if weaviate_key == None:
        logging.error('')
        logging.error('WEAVIATE_API_KEY not set!')
        logging.error('Please set WEAVIATE_API_KEY environment variable.')
        logging.error('')
        return None
        
    logging.info(f'Connecting to Weaviate local instance at {weaviate_host}')

    client = weaviate.connect_to_custom(
        http_host=weaviate_host,
        auth_credentials=AuthApiKey(weaviate_key),
        http_port=80,
        http_secure=False,
        grpc_host="weaviate-grpc.weaviate",
        grpc_port=50051,
        grpc_secure=False,
        skip_init_checks=True,
        additional_config=AdditionalConfig(
            timeout=Timeout(init=30, query=60, insert=120)  # Values in seconds
            )
    )
    return client

def semantic_search(query='computers', limit=2) -> dict:
    print(f'\nSemantic Search, query = {query}.')
    print(f'limit = {limit}')
    response = symbols.query.near_text(
        query=query,
        limit=limit
    )

    print(f'response = {response}')

    return_list = []
    for i in range(limit):
        return_list.append(response.objects[i].properties['name'])
    return return_list


def generative_search(query='computers', task=None, limit=2) -> str:
    print(f'\nPerforming generative search, query = {query}, limit = {limit}.')
    print(f'Prompt: {task}')
    print(f'limit = {limit}')
    response = symbols.generate.near_text(
        query=query,
        limit=limit,
        grouped_task=task
    )

    print(f'response = {response.generated}')

    return response.generated

 
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    # ollama_api_endpoint = os.getenv("OLLAMA_API_ENDPOINT")
    # ollama_vectorizer_model = model = "all-minilm"
    # ollama_generative_model="llama3:8b-instruct-q8_0"
    weaviate_host = os.getenv("WEAVIATE_HOST", "weaviate.weavate")       
    weaviate_key = os.getenv("WEAVIATE_API_KEY")

    #
    # Need to improve the error handling here.
    #
    try:
        client = connect_weaviate_custom()

        symbols = client.collections.get("Symbols")
        print(f'Connected to Weaviate at {weaviate_host}!')
        
        #
        # Build the Gradio user interface.
        #

        #
        # Semantic Search 
        #
        with gr.Blocks(title='Summarizing Financial Data using RAG') as demo:
            gr.Markdown("""# Summarizing Financial Data using Retrieval Augmented Generation (RAG).""")
            semantic_examples = [
                ["Computers"],
                ["Computer Software"],
                ["Pharmaceuticals"],
                ["Consumer Products"],
                ["Commodities"],
                ["Retail"],
                ["Manufacturing"],
                ["Energy"],
                ["National Defense"],
                ["Auto Makers"]
            ]
            gr.Markdown("""### Begin with a search.""")
            semantic_input_text = gr.Textbox(label="Enter a search concept or choose an example below:", value=semantic_examples[0][0])
            gr.Examples(semantic_examples,
                fn=semantic_search,
                inputs=semantic_input_text, label="Example search concepts:"
                )
            limit_slider = gr.Slider(label="Adjust the query return limit. (Optional)",value=2, minimum=1, maximum=5, step=1)
            vdb_button = gr.Button(value="Search the financial vector database.")
            vdb_button.click(fn=semantic_search, inputs=[semantic_input_text, limit_slider], outputs=gr.Textbox(label="Search Results (Filters = Name)"))
            

            #
            # Generative Search 
            # 
            prompt_examples = [
                ["Generate a paragraph that summarizes the given information from a financial perspective for the fiscal year end of December 2024."],
                ["Summarize the information from a financial investment perspective."],
                ["Summarize the potential financial investment risks and rewards."]
            ]

            gr.Markdown("""### Summarize""")
            generative_search_prompt_text = gr.Textbox(label="Enter a summarization task or choose an example below.", value=prompt_examples[0][0])
            gr.Examples(prompt_examples,
                fn=generative_search,
                inputs=[generative_search_prompt_text]
            )
            button = gr.Button(value="Generate the summary.")
            button.click(fn=generative_search,
            inputs=[semantic_input_text, generative_search_prompt_text, limit_slider],
            outputs=gr.Textbox(label="Summary"))
            
        demo.queue(max_size=10)
        demo.launch(server_name='0.0.0.0', server_port=8080, share=False)

    finally:
        client.close()  # Close client gracefully

