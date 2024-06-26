import weaviate
import weaviate.classes as wvc
from weaviate.auth import AuthApiKey
import os
import requests
import json
import ijson
import gradio as gr

def semantic_search(query='computers', limit=2) -> dict:
    print(f'\nSemantic Search, query = {query}.')
    print(f'limit = {limit}')
    response = symbols.query.near_text(
        query=query,
        limit=limit
    )

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
    return response.generated

 
if __name__ == '__main__':
    weaviate_host = os.getenv("WEAVIATE_HOST")       
    weaviate_key = os.getenv("WEAVIATE_API_KEY")

    try:
        client = weaviate.connect_to_custom(
                    http_host=weaviate_host,
                    auth_credentials=AuthApiKey(weaviate_key),
                    http_port=80,
                    http_secure=False,
                    grpc_host="weaviate-grpc.weaviate",
                    grpc_port=50051,
                    grpc_secure=False,
                    skip_init_checks=False,
                    headers={"X-OpenAI-Api-key": os.getenv("OPENAI_API_KEY"),
                        "X-Huggingface-Api-key": os.getenv("HUGGINGFACE_API_KEY")}
                )

        symbols = client.collections.get("Symbols")
        
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
                ["Summarize the information from a financial perspective."],
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
        demo.launch(server_name='0.0.0.0', server_port=8080)

    finally:
        client.close()  # Close client gracefully

