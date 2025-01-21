# weaviate

Running [Weaviate](https://weaviate.io/) on Red Hat OpenShift

## Quickstart

```sh
oc apply -k deploy
```

## Links

- [Weaviate Kubernetes Installation Docs](https://weaviate.io/developers/weaviate/installation/kubernetes).

## Outdated Notes

- Configuration options
  - Set your desired api keys by renaming the default values in the example `values.yaml` file. See lines 153 - 154.
  - You may want to increase the storage `size` to something larger. See line 88.
  - This example `values.yaml` enables the following sections:
    - `apikey`
    - `text2vec-huggingface`
    - `text2vec-openai`
    - `generative-openai`

Add the weaviate repo to the helm configuration.

```sh
helm repo add weaviate https://weaviate.github.io/weaviate-helm
```

Install Weaviate

```sh
helm upgrade --install weaviate weaviate/weaviate --namespace ${PROJECT} --values ./values.yaml
```

- Optionally, expose the Weaviate service as a route. If using DevSpaces you can use
the weaviate service (<http://weaviate.weaviate>) directly.

```sh
oc create route edge weaviate --service=weaviate --insecure-policy='Redirect' -n ${PROJECT}

WEAVIATE_HOST=$(oc get routes weaviate -n ${PROJECT} -o jsonpath='{.spec.host}')
```

### Test using the route

```sh
export WEAVIATE_HOST
curl -sL https://"${WEAVIATE_HOST}" | jq .
```

### Test using the service name

```sh
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

### Use the [Weaviate Cloud Console](https://console.weaviate.cloud/) to make GraphQL queries

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
