# weaviate

Running [Weaviate](https://weaviate.io/) on Red Hat Openshift

## My test enviroment
- Openshift (v4.13.6)
- `helm` (v3.8.1)
- A workstation to run the `oc` and `helm` [command line tools](https://mirror.openshift.com/pub/openshift-v4/clients/).

### Installation
1) Install the `oc` and `helm` programs on your client workstation.

2) Login to Openshift and create a project.

```bash
PROJ=weaviate
oc new-project ${PROJ}
```

3) Begin by reviewing the [Weaviate Kubernetes Installation docs](https://weaviate.io/developers/weaviate/installation/kubernetes). As a quick start, use the [example helm chart values file](values.yaml)  in this repo.
  - Configuration options
    - Set your desired api keys by renaming the default values in the example `values.yaml` file. See lines 153 - 154.
    - If deploying in the [Developer Sandbox](https://developers.redhat.com/developer-sandbox) change the storage `size` to `5Gi` or less. See line 88.
    - This example `values.yaml` enables the following sections:
        - `apikey`
        - `text2vec-huggingface`
        - `generative-openai`

4) Configure and run the helm installer and wait for the weaviate pod to become ready.

- Add the weaviate repo to the helm configuration.

```bash
helm repo add weaviate https://weaviate.github.io/weaviate-helm
```
- Install Weaviate
```bash
helm upgrade --install weaviate weaviate/weaviate --namespace ${PROJ} --values ./values.yaml
```

5) Expose the Weaviate service as a route
```bash
oc create route edge weaviate --service=weaviate --insecure-policy='Redirect'
```

## Testing
```bash
export WEAVIATE_URL=https://$(oc get routes weaviate -n ${PROJ} -o jsonpath='{.spec.host}')
curl ${WEAVIATE_URL}
```

Sample output
```json
{
  "links": {
    "href": "/v1",
    "name": "api v1",
    "documentationHref": "https://weaviate.io/developers/weaviate/current/"
  }
}
```
## Sample Applications

1) Create a python virtual environment and try a few of the [example clients](src). The first two python examples expect the `WEAVIATE_URL` and `WEAVIATE_API_KEY` variables to be set.
```bash
python -m venv ~/venv
source ~/venv/bin/activate
cd src
pip install -r requirements.txt
```
```bash
export WEAVIATE_URL=https://$(oc get routes weaviate -n ${PROJ} -o jsonpath='{.spec.host}')
```
```bash
export WEAVIATE_API_KEY='weaviate-api-key-from-values-file-above'
```

2) Test the connection with the python sdk.

```bash
python 00-test-connection.py 
```

Sample output:
```bash
WEAVIATE_URL https://weaviate.apps.openshift.com is_ready() = True

cluster.get_nodes_status(): [{'batchStats': {'queueLength': 0, 'ratePerSecond': 0}, 'gitHash': '8172acb', 'name': 'weaviate-0', 'shards': [{'class': 'Article', 'name': '7dLd8SoAYAEx', 'objectCount': 100}, {'class': 'Author', 'name': 'HaNbOTa3gorn', 'objectCount': 128}, {'class': 'Question', 'name': 's592CBYYm2N4', 'objectCount': 10}], 'stats': {'objectCount': 538, 'shardCount': 4}, 'status': 'HEALTHY', 'version': '1.21.0'}]
```

3) Create a schema and import some objects.

This example requires a [HuggingFace api token](https://huggingface.co/settings/tokens) to create vectors.
```bash
export HUGGINGFACE_API_KEY=your-huggingface-api-key
```
```bash
python 01-create-schema-import-data.py
```
The first time running may produce the following error if the huggingface transformer model is not quite ready.
```
{'error': [{'message': 'update vector: failed with status: 503 error: Model sentence-transformers/msmarco-bert-base-dot-v5 is currently loading estimated time: 20'}]}
```

Sample output:
```
WEAVIATE_URL: https://weaviate-weaviate.apps.ocp.sandbox1234.openshift.com

WEAVIATE_URL: https://weaviate-weaviate.apps.ocp.sandbox1234.openshift.com is_ready() = True

Creating a class using the text2vec-huggingface vectorizer.
Question class already exists, skipping
importing question: 1
importing question: 2
...
```

4) Perform a semantic search.

```bash
python 02-semantic-search.py
```

Sample output:
```json
{
    "data": {
        "Get": {
            "Question": [
                {
                    "_additional": {
                        "score": "0.0040983604"
                    },
                    "answer": "the atmosphere",
                    "question": "Changes in the tropospheric layer of this are what gives us weather"
                },
                {
                    "_additional": {
                        "score": "0.004032258"
                    },
                    "answer": "Elephant",
                    "question": "It's the only living mammal in the order Proboseidea"
                },
                {
                    "_additional": {
                        "score": "0.003968254"
                    },
                    "answer": "the diamondback rattler",
                    "question": "Heaviest of all poisonous snakes is this North American rattlesnake"
                }
            ]
        }
    }
}

```

5) Perform a retrieval augmented generative search.

![rag-demo](images/retrieval-augmented-generation.jpg "retrieval augmented generative search")

This generative AI example requires an [OpenAI API token](https://platform.openai.com/account/api-keys).
```
export OPENAI_API_KEY=my_openai_api_key
```
```
python 03-generative-search.py
```
Sample output:
```json
{
    "data": {
        "Get": {
            "Question": [
                {
                    "_additional": {
                        "generate": {
                            "error": null,
                            "singleResult": "An elephant is a really big animal with a long trunk, big ears, and a strong body. They are usually gray in color. Elephants are very smart and friendly. They live in places called forests and grasslands. They eat lots of plants and fruits. They use their long trunk to grab food and drink water. Elephants also use their trunk to say hello to other elephants by touching them gently. They have big ears that help them hear really well. Elephants are very strong and can carry heavy things with their trunk. They are also great swimmers and love to play in the water. Elephants are loved by many people because they are so amazing and special!"
                        }
                    },
                    "answer": "Elephant",
                    "category": "ANIMALS",
                    "question": "It's the only living mammal in the order Proboseidea"
                }
    }
}
```
6) Run the Gradio front end application example and visit
the port reported with a web browser.
```bash
python 05-gradio
```

7) Use the [Weaviate Cloud Console](https://console.weaviate.cloud/) to make GraphQL queries.

- Add an Openshift route for your external cluster.
- Navigate to the query editor and configure the header.
```json
{
  "Authorization" : "Bearer my-weaviate-api-key",
  "X-HuggingFace-Api-Key" : "my-huggingface-api-key"
}
```

- Enter the following sample GraphQL:
```
{
  Get {
    Question (
      nearText: {
        concepts: ["biology"],
        distance: 0.6 
        moveAwayFrom: {
          concepts: ["technology"],
          force: 0.45
        }
      }
    ){
      answer
      _additional {
        certainty # only supported if distance==cosine.
        distance  # always supported
      }
    }
  }
}
```

Sample output:
```json
{
  "data": {
    "Get": {
      "Question": [
        {
          "_additional": {
            "certainty": 0.9416711330413818,
            "distance": 0.116657734
          },
          "answer": "Elephant"
        },
        {
          "_additional": {
            "certainty": 0.9404493570327759,
            "distance": 0.119101286
          },
          "answer": "Liver"
        },
        {
          "_additional": {
            "certainty": 0.9401318430900574,
            "distance": 0.119736314
          },
          "answer": "DNA"
        },
        {
          "_additional": {
            "certainty": 0.9372586607933044,
            "distance": 0.12548268
          },
          "answer": "the atmosphere"
        },
        {
          "_additional": {
            "certainty": 0.9305243492126465,
            "distance": 0.1389513
          },
          "answer": "species"
        },
        {
          "_additional": {
            "certainty": 0.9297976493835449,
            "distance": 0.1404047
          },
          "answer": "the nose or snout"
        },
        {
          "_additional": {
            "certainty": 0.9294309914112091,
            "distance": 0.14113802
          },
          "answer": "the diamondback rattler"
        },
        {
          "_additional": {
            "certainty": 0.9264078438282013,
            "distance": 0.14718431
          },
          "answer": "Sound barrier"
        },
        {
          "_additional": {
            "certainty": 0.9256481826305389,
            "distance": 0.14870363
          },
          "answer": "Antelope"
        },
        {
          "_additional": {
            "certainty": 0.9158381223678589,
            "distance": 0.16832376
          },
          "answer": "wire"
        }
      ]
    }
  }
}
```

8) Delete the schema if necessary.

```bash
python 04-delete-schema.py
```
