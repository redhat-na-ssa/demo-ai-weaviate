import json
import requests
import numpy as np
from numpy.linalg import norm

# This example shows how to use the Ollama API to generate embeddings for a given input
# The embeddings are then used to calculate the cosine similarity between the embeddings
# of two different inputs
#
# NOTE: this example requires the ollama API to be runningon the same machine as this script
# You can run the API by running `ollama serve` in the root of the ollama repository
#
# This example uses the all-minilm model, which is a small model that is good for
# understanding the structure of a sentence
#
# For more information about the API, see the API documentation:
# https://ollama.readthedocs.io/en/latest/api.html

# NOTE: ollama must be running for this to work, start the ollama app or run `ollama serve`

model = 'nomic-embed-text:latest'
model = 'all-minilm:latest'

def generate(input, context):
    r = requests.post('http://localhost:11434/api/embed',
                      json={
                          'model': model,
                          'input': input,
                      },
                      stream=False)
    r.raise_for_status()

    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get('embeddings', '')

        if 'error' in body:
            raise Exception(body['error'])

        if body.get('total_duration', True):
            return body['embeddings']

def main():
    context = [] # the context stores a conversation history, you can use this to make the model more context aware
    user_input = 'kitten'
    kitten = generate(user_input, context)[0]

    user_input = 'cat'
    cat = generate(user_input, context)[0]
    cosine = np.dot(kitten, cat)/(norm(kitten)*norm(cat))
    print(f'Kitten/Cat Cosine Similarity: {cosine:.2f}')
    
    user_input = 'dog'
    dog = generate(user_input, context)[0]
    cosine = np.dot(kitten, dog)/(norm(kitten)*norm(dog))
    print(f'Kitten/Dog Cosine Similarity: {cosine:.2f}')
    
    user_input = 'wolf'
    wolf = generate(user_input, context)[0]
    cosine = np.dot(kitten, wolf)/(norm(kitten)*norm(wolf))
    print(f'Kitten/Wolf Cosine Similarity: {cosine:.2f}')
    
    user_input = 'guitar'
    guitar = generate(user_input, context)[0]
    cosine = np.dot(kitten, guitar)/(norm(kitten)*norm(guitar))
    print(f'Kitten/Guitar Cosine Similarity: {cosine:.2f}')

if __name__ == "__main__":
    main()