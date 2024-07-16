# Summarizing Financial Data with a RAG workflow using [Weaviate](https://weaviate.io/) and [Red Hat OpenShift:](https://developers.redhat.com/developer-sandbox)

![rag-demo](images/retrieval-augmented-generation.jpg "retrieval augmented generative search")
*High Level Components*

### Overview
This demonstration imports and syncronizes financial data from [AlphaVantage](https://www.alphavantage.co)
into [Weaviate's vector database](https://weaviate.io) which in turn uses a large language model to generate a summary 
in a traditional RAG workflow.

The Weaviate database is installed on Openshift as a stateful set providing
a data parallel enterprise deployment. For the application developer, Openshift DevSpaces offers a full IDE experience
within a Kubernetes environment. Finally, a simple example application based on Hugging Face's Gradio framework provides a user front-end.

![dataflow](images/dataflow.jpg "Dataflow")
*Dataflow*

To build the vector database, a number of company overviews are downloaded using 
[AlphaVantage's Stock Market API](https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=demo)
and imported into Weaviate. This represents a private knowledgebase. Each overview 
consists of a short description along with sampling of financial metrics such as market
capitalization, book value and earnings per share just to name a few. A user can then query 
the database using a natural language and Weaviate will return companies that are most 
similar to the concept. Finally, a generative search is performed using the
[llama3](https://github.com/meta-llama/llama3.git) large language model (LLM) to generate a 
financial summary which is presented to the user. It is important to note that the summary is 
based on the financial data from the original company overview database and not the LLM.  

![financial-rag](images/finance-rag.png "Financial summary using RAG")
*Application Screen Shot*

### What's needed:
- Access to [Red Hat Openshift](https://developers.redhat.com/developer-sandbox).
- An [AlphaVantage API key](https://www.alphavantage.co/support/#api-key) if you want to refresh the stock symbol data.
- An [Ollama server running on Openshift](https://github.com/williamcaban/ollama-ubi) installed 
in the `ollama` namespace.
  - The `all-minilm` and `llama3` models should be [pulled](https://github.com/ollama/ollama/blob/main/docs/api.md#pull-a-model) after install.
- A Weaviate instance installed in the `weaviate` namespace.
- [Red Hat Build for Apache Camel](https://github.com/joshdreagan/av-overview-sync.git) installed in 
the `camel` namespace.

### Environment Variables

Name | Description | Default Value
--- | --- | ---
WEAVIATE_API_KEY | Weaviate Admin API Key | None
WEAVIATE_HOST | The hostname of the Weaviate service | weaviate.weaviate
ALPHA_VANTAGE_API_KEY | AlphaVantage API Key | None
OLLAMA_HOST | The hostname of the Openshift Ollama service | http://ollama-svc.ollama
OLLAMA_VECTORIZER | The name of the Ollama vectorizer model | all-minilm
OLLAMA_LLM | The name of the Ollama language model | llama3:8b-instruct-q8_0

### Why run Weaviate On Openshift?
- Support for [Distributed Architectures](https://weaviate.io/developers/weaviate/concepts/replication-architecture).
- A Great Developer Experience (Easily move code -> containers)
- Access your cluster via the Weaviate Cloud Console with external routes.
- Security (Doesn't run your containers as root)

### Developer Tools: Eclipse-Che/DevSpaces
- A full IDE experience with a code debugger.
- Leverage many VSCode extensions.
- In cluster terminal with CLI access to the Openshift API.
- Deploy and test your app with port forwarding.
- GitHub integration improves workflow efficiency.
- Environment variables are read in as secrets.
- DevSpaces is a no-cost add-on to Openshift

### Getting Started
- Login to [Openshift](https://developers.redhat.com/developer-sandbox) and launch Openshift DevSpaces.
- Create a new workspace by importing the git url `https://github.com/redhat-na-ssa/demo-ai-weaviate`


### Setup DevSpaces for Python Development
1. **VSCode Extensions** -> Confirm the Python IntelliSense extension is installed and enabled.
1. **View -> Command Palette** -> Enter: `dev spaces: open openshift console`.
1. Use the Openshift Web UI to **create a secret with environment variables**.
   * **Secrets -> Create** and **Save** a new secret (from yaml) using this [example](che-env-vars.yaml). You may have to add a `metadata.namespace` field that contains your Developer Sandbox namespace and choose *Create*.
   * **Edit ->** Scroll down to the data section and change the values in the secret to match your environment variables needed for the API keys and Weaviate URL then save. 
   *  Now choose *Add Secret to workload*. DevSpaces will likely restart.
1. Create a new python virtual environment
      * *Terminal -> New Terminal**
      * `python -m venv .venv`
      * `source .venv/bin/activate`
      * `pip install -r src/requirments.txt`
1. Follow [these instructions](install-weaviate.md) to **install Weaviate**.
1. Verify the connection to the Weaviate service.
```bash
python src/00-test-connection.py
```
2. Import the data. An important note is that the hostname and model name of the
ollama vectorizer gets embedded into the Weaviate collection. This means the `03-app.py`
application expects to find a Weaviate instance with a vectorizer configured the
same.
```bash
python src/01-import-csv.py
```
3. Validate the Weaviate collection.
```bash
python src/02-check-collection.py
```
4. Run the application. DevSpaces should setup port forwarding so the application will appear in a web browser.
```bash
python src/03-app.py
```
### Move the app into production.
1. From the terminal, create an Openshift application.
```bash
oc new-app python~https://github.com/redhat-na-ssa/demo-ai-weaviate#v4 --context-dir=/src --name=rag \
--env WEAVIATE_HOST=weaviate.weaviate --env WEAVIATE_API_KEY=your_weaviate_admin-api-key --env OPENAI_API_KEY=your_openai_api_key
```
2. Expose the app with a route.
```bash
oc create route edge --service rag --insecure-policy='Redirect'
```

### Clean up
```bash
oc delete all --selector=app=rag
helm uninstall weaviate
```

#### Remove the Openshift storage.
```bash
oc delete pvc weaviate-data-weaviate-0 weaviate-data-weaviate-1
```

### Additional ways to get access to Openshift.
- Create a mini-cluster by [installing Code Ready Containers](https://www.okd.io/crc/)
- Install an [OKD cluster](https://www.okd.io/installation/) and Eclipse-Che.
- Install an [Openshift](https://www.redhat.com/en/technologies/cloud-computing/openshift) cluster and DevSpaces.
- As a managed service from any of the major cloud providers.

