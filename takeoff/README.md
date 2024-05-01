# Takeoff Helm Chart

This is our example template of a Helm chart for deploying Takeoff in Kubernetes. 

## Prerequisites

### Docker Pull Secret

In order to pull the Takeoff container you need to have logged into your account which has been given permission to access the Takeoff container in DockerHub. Then you can create the secret with the following command:

```bash
kubectl create secret generic takeoff-regcred --from-file=.dockerconfigjson=<path/to/.docker/config.json> --type=kubernetes.io/dockerconfigjson
```

## Installing the Chart

```bash
helm install takeoff-helm . --values values.yaml       
```