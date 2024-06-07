# Building Powerful Applications with [Weaviate](https://weaviate.io/) and [Red Hat OpenShift:](https://developers.redhat.com/developer-sandbox) A Retrieval-Augmented Generation Workflow

## What we will build.
![rag-demo](images/retrieval-augmented-generation.jpg "retrieval augmented generative search")

### Overview
The RAG demonstration is built on the Weaviate quick start example that vectorizes and imports a few Jeopardy-style questions
using a Hugging Face text-to-vector module. Using Weaviate's Python SDK, similarity searches are performed in vector space which are used to construct a prompt that inferences
a large language model hosted by OpenAI. The Weaviate database is installed on Openshift as a stateful set providing
a data parallel enterprise deployment. For the application developer, Openshift DevSpaces offers a full IDE experience
within a Kubernetes environment. Finally, a simple example application based on Hugging Face's Gradio framework provides a front-end to an end user.

### What's needed:
- Access to a free [Developer Sandbox for Red Hat Openshift](https://developers.redhat.com/developer-sandbox).
- A [HuggingFace API key](https://huggingface.co/settings/tokens).
- An [OpenAI API key](https://platform.openai.com/account/api-keys).

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
- Login to the [Developer Sandbox for Red Hat Openshift](https://developers.redhat.com/developer-sandbox) and launch Openshift DevSpaces.
- Create a new workspace by importing the git url `https://github.com/redhat-na-ssa/demo-ai-weaviate`


### Setup DevSpaces for Python Development

1. **VSCode Extensions** -> Confirm the Python IntelliSense extension is installed and enabled.
1. **View -> Command Palette** -> Enter: `dev spaces: open openshift console`.
1. Use the Openshift Web UI to **create a secret with environment variables**.
   * **Secrets -> Create** and **Save** a new secret (from yaml) using this [example](resources/che-env.yaml). You may have to add a `metadata.namespace` field that contains your Developer Sandbox namespace and choose *Create*.
   * **Edit ->** Scroll down to the data section and change the values in the secret to match your environment variables needed for the API keys and Weaviate URL then save. 
   *  Now choose *Add Secret to workload*. DevSpaces will likely restart.
1. Create a new python virtual environment
      * *Terminal -> New Terminal**
      * `python -m venv .venv`
      * `source .venv/bin/activate`
      * `pip install -r src/requirments.txt`
1. Follow [these instructions](install-weaviate.md) to **install Weaviate**.

1. Run a few python test clients from the `src` directory. Clients 06 and 07 are WIP and 
require the [wikipedia parquet data file](https://koz-data.s3.us-east-2.amazonaws.com/wiki_simple_100k.parquet).
```bash
python src/00-test-connection.py
```
```bash
python src/05-gradio.py
```

### Move the app into production.
1. From the terminal, create an Openshift application.
```bash
oc new-app python~https://github.com/bkoz/weaviate --context-dir=/src --name=rag
```

2. Add the secret to the deployment.
```bash
oc set env --from=secret/che-env-vars deployment/rag
```

3. Expose the app with a route.
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

