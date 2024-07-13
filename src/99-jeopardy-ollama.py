import gradio as gr
from huggingface_hub import InferenceClient
import weaviate.classes as wvc
import weaviate
from weaviate.auth import AuthApiKey
import logging
import os
import requests
import json
import weaviate

#
# Environment variables
#
# export WEAVIATE_API_KEY=your-weaviate-api-key
# export WEAVIATE_HOST=weaviate.weaviate
# export OLLAMA_API_ENDPOINT=https://my-ollama-api-server.domain.com

ollama_api_endpoint = os.getenv("OLLAMA_API_ENDPOINT", "http://localhost:11434")
ollama_vectorizer_model = model = "all-minilm"
ollama_generative_model="llama3"

logging.basicConfig(level=logging.INFO)
logging.info(f'OLLAMA_API_ENDPOINT = {ollama_api_endpoint}')

def connect_weaviate_custom():
    weaviate_host = os.getenv("WEAVIATE_HOST")     
    weaviate_key = os.getenv("WEAVIATE_API_KEY")

    logging.basicConfig(level=logging.INFO)
    logging.info(f'OLLAMA_API_ENDPOINT = {ollama_api_endpoint}')
    if weaviate_host == None:
        logging.error('WEAVIATE_HOST not set')
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
        skip_init_checks=True
    )
    return client

def connect_weaviate_embedded():
    logging.basicConfig(level=logging.INFO)
    logging.info('Connecting to Weaviate embedded instance')
    client = weaviate.connect_to_embedded(
        environment_variables={"ENABLE_MODULES": "text2vec-ollama,generative-ollama"},
        version="1.25.6"
    )
    return client

# client = connect_weaviate_custom()
client = connect_weaviate_embedded()

if client.is_ready():
    logging.info('')
    logging.info(f'Found {len(client.cluster.nodes())} Weaviate nodes.')
    logging.info('')
    for node in client.cluster.nodes():
        logging.info(node)
        logging.info('')
    logging.info(f'client.get_meta(): {client.get_meta()}')
else:
    logging.error("Client is not ready")

client.collections.delete_all()

# lets create the collection, specifing our base url accordingling
questions = client.collections.create(
    "Question",
    vectorizer_config=wvc.config.Configure.Vectorizer.text2vec_ollama(
        api_endpoint=ollama_api_endpoint,
        model=ollama_vectorizer_model
    ),
    generative_config=wvc.config.Configure.Generative.ollama(
        api_endpoint=ollama_api_endpoint,
        model=ollama_generative_model
    )
)
resp = requests.get('https://raw.githubusercontent.com/databyjp/wv_demo_uploader/main/weaviate_datasets/data/jeopardy_1k.json')
data = json.loads(resp.text)

question_objs = list()
for i, d in enumerate(data):
    question_objs.append({
        "answer": d["Answer"],
        "question": d["Question"],
        "category": d["Category"],
        "air_date": d["Air Date"],
        "round": d["Round"],
        "value": d["Value"]
})

logging.info('Importing 1000 Questions...')
questions = client.collections.get("Question")
questions.data.insert_many(question_objs)
logging.info('Finished Importing Questions')

logging.info(f'Collection: {questions}')

# def respond(query):

#     response = questions.query.near_text(
#         query=query,
#         limit=1
#     )

#     return response.objects[0].properties 

def respond(query='computers', task='Summarize', limit=1) -> str:
    print(f'\nPerforming generative search, query = {query}, limit = {limit}.')
    print(f'Prompt: {task}')
    print(f'limit = {limit}')
    response = questions.generate.near_text(
        query=query,
        limit=limit,
        grouped_task=task
    )
    return response.generated

with gr.Blocks(title="Search the Jeopardy Vector Database. (powered by Weaviate and Ollama)") as demo:
            gr.Markdown("""# Search and summarize the Jeopardy Vector Database. (Powered by Weaviate and Ollama)""")
            semantic_examples = [
                ["Nature"],
                ["Music"],
                ["Wine"],
                ["Consumer Products"],
                ["Sports"],
                ["Fishing"],
                ["Food"],
                ["Weather"]
            ]
            semantic_input_text = gr.Textbox(label="Enter a search concept or choose an example below:", value=semantic_examples[0][0])
            gr.Examples(semantic_examples, inputs=semantic_input_text, label="Example search concepts:")
            vdb_button = gr.Button(value="Search and Summarize the Jeopardy Vector Database.")
            vdb_button.click(fn=respond, inputs=[semantic_input_text], outputs=gr.Textbox(label="Search Results"))
            

if __name__ == "__main__":
    demo.launch(server_name='0.0.0.0', server_port=8080)
