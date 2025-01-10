# weaviate

Running [Weaviate](https://weaviate.io/) on Red Hat OpenShift

## My test enviroment

- OpenShift (v4.13.6)
- [`helm`](https://helm.sh/docs/intro/install/) (v3.8.1)
- A workstation to run the `oc` and `helm` [command line tools](https://mirror.openshift.com/pub/openshift-v4/clients/).

### Installation

1) Install the `oc` and [`helm`](https://helm.sh/docs/intro/install/) programs on your client workstation.

2) Login to OpenShift and create a new project with a unique name. If you are using the Developer Sandbox
for Red Hat OpenShift a project will already exist.

To check for the existence of a project run `oc project`, otherwise use `oc new-project` to create one.

```bash
PROJ=weaviate
```

```bash
oc new-project $PROJ
```

3) Begin by reviewing the [Weaviate Kubernetes Installation docs](https://weaviate.io/developers/weaviate/installation/kubernetes). As a quick start, use the [example helm chart values file](values.yaml)  in this repo.

- Configuration options
  - Set your desired api keys by renaming the default values in the example `values.yaml` file. See lines 153 - 154.
  - You may want to increase the storage `size` to something larger. See line 88.
  - This example `values.yaml` enables the following sections:
    - `apikey`
    - `text2vec-huggingface`
    - `text2vec-openai`
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

5) Optionally, expose the Weaviate service as a route. If using DevSpaces you can use
the weaviate service (<http://weaviate.weaviate>) directly.

```bash
oc create route edge weaviate --service=weaviate --insecure-policy='Redirect' -n $PROJ
```

### Test using the route

```bash
export WEAVIATE_HOST=$(oc get routes weaviate -n ${PROJ} -o jsonpath='{.spec.host}')
curl https://"${WEAVIATE_HOST}" | jq .
```

### Test using the service name

```bash
export WEAVIATE_HOST="https://" + $(oc get routes weaviate -n ${PROJ} -o jsonpath='{.spec.host}')
curl http://weaviate.weaviate | jq .
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

1) Use the [Weaviate Cloud Console](https://console.weaviate.cloud/) to make GraphQL queries.

- Add an OpenShift route for your external cluster.
- Navigate to the query editor and configure the header as follows.

```json
{
  "Authorization" : "Bearer my-weaviate-api-key",
  "X-HuggingFace-Api-Key" : "my-huggingface-api-key"
}
```

- Enter the following sample GraphQL:

```json
{
  Get {
    Symbols(
       nearText: {
        concepts: ["Computers"]
      } limit: 2
    ) {
      symbol
      name
      description
    }
  }
}
```

Example output

```json
{
  "data": {
    "Get": {
      "Symbols": [
        {
          "description": "Advanced Micro Devices, Inc. (AMD) is an American multinational semiconductor company based in Santa Clara, California, that develops computer processors and related technologies for business and consumer markets. AMD's main products include microprocessors, motherboard chipsets, embedded processors and graphics processors for servers, workstations, personal computers and embedded system applications.",
          "name": "Advanced Micro Devices Inc",
          "symbol": "AMD"
        },
        {
          "description": "Microsoft Corporation is an American multinational technology company which produces computer software, consumer electronics, personal computers, and related services. Its best known software products are the Microsoft Windows line of operating systems, the Microsoft Office suite, and the Internet Explorer and Edge web browsers. Its flagship hardware products are the Xbox video game consoles and the Microsoft Surface lineup of touchscreen personal computers. Microsoft ranked No. 21 in the 2020 Fortune 500 rankings of the largest United States corporations by total revenue; it was the world's largest software maker by revenue as of 2016. It is considered one of the Big Five companies in the U.S. information technology industry, along with Google, Apple, Amazon, and Facebook.",
          "name": "Microsoft Corporation",
          "symbol": "MSFT"
        }
      ]
    }
  }
}
```
