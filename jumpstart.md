# JumpStart your [Vector Database](https://weaviate.io/) to enterprise scale with [OKD](httos://okd.io)

## Agenda

### Different ways to get access to Openshift
- The easiest path is to signup for a [Developer Sandbox](https://developers.redhat.com/developer-sandbox)
- Create a mini-cluster by [installing Code Ready Containers](https://www.okd.io/crc/)
- Create a community cluster by [installing OKD](https://www.okd.io/installation/) and the [Eclipse-Che] operator.
- Create an [Openshift](https://www.redhat.com/en/technologies/cloud-computing/openshift) cluster and the [DevSpaces] operator.

### [Install Weaviate](README.md)

### Developer Workflow
- Launch the Eclipse-Che/DevSpaces dashboard.
- Add a new workspace by cloning https://github.com/bkoz/weaviate
- Install the VSCode python extension.
- Create a python virtual environment (Shift-Command-P)
- Open a terminal (Control `)
- Test the weaviate service
```
curl ${WEAVIATE_URL} | jq
```

### Add environment variables using secrets
```
oc apply -f resources/che-env-vars.yaml
```
### GitHub integration

### Port forwarding

