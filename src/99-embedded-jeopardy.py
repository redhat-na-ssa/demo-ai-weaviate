import gradio as gr
from huggingface_hub import InferenceClient
import weaviate.classes as wvc
import weaviate
from weaviate.auth import AuthApiKey
import logging
import os
import requests
import json

logging.basicConfig(level=logging.INFO)

client = weaviate.connect_to_embedded(
    headers={
        "X-Huggingface-Api-Key": os.environ["HUGGINGFACE_API_KEY"]
    }
)

if client.is_ready():
    logging.info('')
    logging.info(f'Found {len(client.cluster.nodes())} Weaviate nodes.')
    logging.info('')
    for node in client.cluster.nodes():
        logging.info(node)
        logging.info('')

client.collections.delete_all()

questions = client.collections.create(
    name="Question",
    vectorizer_config=wvc.config.Configure.Vectorizer.text2vec_huggingface(wait_for_model=True),  
    generative_config=wvc.config.Configure.Generative.openai()  
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

print(questions)

def respond(query):

    response = questions.query.near_text(
        query=query,
        limit=1
    )

    return response.objects[0].properties 

with gr.Blocks(title="Search the Jeopardy Vector Database powered by Weaviate") as demo:
            gr.Markdown("""# Search the Jeopardy Vector Database powered by Weaviate""")
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
            vdb_button = gr.Button(value="Search the Jeopardy Vector Database.")
            vdb_button.click(fn=respond, inputs=[semantic_input_text], outputs=gr.Textbox(label="Search Results"))
            

if __name__ == "__main__":
    demo.launch(server_name='0.0.0.0', server_port=8080)
