### Download data to `data/wiki_simple_100k.parquet`

# Link: [google drive](https://drive.google.com/file/d/1_sBvE9RKYUSHGSfJomiLf-2d7O6SUIoS/view)

## ☁️☁️ Configure the Weaviate Cloud Instance ☁️☁️
### Free 14 day sandbox here: https://console.weaviate.cloud/

import os
import weaviate
import json
import weaviate_utils
import os
import logging
import requests

logging.basicConfig(level=logging.INFO)

client = weaviate_utils.weaviate_connection()
logging.info('\nclient.isReady(): %s', client.is_ready())
logging.info('cluster.get_nodes_status(): %s', client.cluster.get_nodes_status())


"""## 🔎🔎All the ways you can search your data:🔍🔍

### 1. Classic Word Search
- Basic word matching. Look for the occurence of a word in the document.

### 2. Vector Search
- Find closest object vectors closest to query vector. Fetches objects the have similar meaning to the query.

### 3. Hybrid Search - combine word and semantic match.
- Perform both word and vector search and then combine the results.

### 4. Generative Search - search and interpret with an LLM.
- Search for semantically relevant documents to a prompt and then provide them as context to a LLM to guide its generation.

### 1. Classic Word Search
"""

where_filter = {
  "path": ["title"],
  "operator": "Like",
  "valueString": "Dog"
}

query_result = (
  client.query
  .get("Article", ["title", "text","wiki_id"])
  .with_where(where_filter)
  .with_limit(3)
  .do()
)

print(json.dumps(query_result, indent=2))

where_filter = {
  "path": ["title"],
  "operator": "Like",
  "valueString": "animals"
}

query_result = (
  client.query
  .get("Article", ["title", "text","wiki_id"])
  .with_where(where_filter)
  .do()
)

# print(query_result)

print(query_result['data']['Get']['Article'][0]['title']+'\n'+query_result['data']['Get']['Article'][0]['text'])

query_result

"""### 2. Vector Search"""

def semantic_search(query):
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
        .with_limit(3)
        .do()
    )

    result = response['data']['Get']['Article']

    return result

def print_result(result):
    for item in result:
        print(f"\033[95m{item['title']} ({item['views']}) {item['_additional']['distance']}\033[0m")
        print(f"\033[4m{item['url']}\033[0m")
        print(item['text'])
        print()

print("***** Vector Search ******")
query_result = semantic_search('cutest animals')

print_result(query_result)

query_result = semantic_search("a programming language used for machine learning")

print_result(query_result)

"""### ... but wait ... this is a Multi-Lingual Model! 🗣❗️

 - You can use it to perform multilingual search! Search in one language that model understands and recieve relevant documents in any language!
"""

# This is a multi-lingual model so it can take in queries in different languages!

#good movies in hindi

query_result = semantic_search("महान फिल्में")

print_result(query_result)

#vacation spots in Farsi

query_result = semantic_search("مکان های تعطیلات")

print_result(query_result)

# GREAT ACTION movies in chinese
query_result = semantic_search("很棒的电影")

print_result(query_result)

"""### 3. Hybrid Search:

- Getting the best of both world!
"""

response = (
    client.query
    .get("Article", ["title", "text"])
    .with_hybrid(
        query="The Dark Knight",
        alpha=0
    )
    #.with_additional(["score", "explainScore"])
    .with_limit(3)
    .do()
)

print(json.dumps(response, indent=2))

response = (
    client.query
    .get("Article", ["title", "text"])
    .with_hybrid(
        query="The Dark Knight",
        alpha=1
    )
    #.with_additional(["score", "explainScore"])
    .with_limit(3)
    .do()
)

print(json.dumps(response, indent=2))

"""### 4. Generative Search:
- Attaching your search engine outputs to a LLM to generate with!/
"""

print("********* Semantic Search ********")
bb_res = semantic_search("famous basketball player")
print_result(bb_res)

generatePrompt = "Write me some interview questions I can ask {title} here is some information about them {text}"

print("********* Generative Search ********")

result = (
  client.query
  .get("Article", ["title","text"])
  .with_generate(single_prompt=generatePrompt) # Pass in each obj 1 at a time
  .with_near_text({
    "concepts": ["famous basketball players"]
  })
  .with_limit(1)
).do()

print(json.dumps(result, indent=2))

print("Generated Text:\n" + result['data']['Get']['Article'][0]['_additional']['generate']['singleResult']+"\n")


print("Relevant Context:\n" + result['data']['Get']['Article'][0]['title']+"\n")

"""#### Passing all relevant documents to complete a Task specified in the Prompt: Grouped Task"""

generateTask = "Which of these players in {text} is the most accomplished. Choose atleast one"

result = (
  client.query
  .get("Article", ["title","text"])
  .with_generate(grouped_task=generateTask)
  .with_near_text({
    "concepts": ["famous basketball players"]
  })
  .with_limit(1)
).do()

print("Generated Text:\n" + result['data']['Get']['Article'][0]['_additional']['generate']['groupedResult']+"\n"+"\nArticle Titles Provided as Context:\n")

k = [print(result['data']['Get']['Article'][i]['title']+"\n") for i in range(len(result['data']['Get']['Article']))]

generateTask = "Explain why these {text} results are all similar "

result = (
  client.query
  .get("Article", ["title","text"])
  .with_generate(grouped_task=generateTask)
  .with_near_text({
    "concepts": ["famous basketball players"]
  })
  .with_limit(1)
).do()

print("Generated Text:\n" + result['data']['Get']['Article'][0]['_additional']['generate']['groupedResult']+"\n\nArticle Titles Provided as Context:\n")

k = [print(result['data']['Get']['Article'][i]['title']+"\n") for i in range(len(result['data']['Get']['Article']))]

generateTask = "Tell me a one paragraph story where these people {title} fight each other, here's some information about them {text}"

result = (
  client.query
  .get("Article", ["title",'text'])
  .with_generate(grouped_task=generateTask)
  .with_near_text({
    "concepts": ["famous basketball players"]
  })
  .with_limit(1)
).do()

print("Generated Text:\n" + result['data']['Get']['Article'][0]['_additional']['generate']['groupedResult']+"\n\nArticle Text Provided as Context:\n")

k = [print(result['data']['Get']['Article'][i]['title']+"\n") for i in range(len(result['data']['Get']['Article']))]

"""### Learn more in the Weaviate Docs
![image.png](attachment:image.png)
"""

