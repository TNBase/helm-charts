# Takeoff Helm Chart

This is our example template of a Helm chart for deploying Takeoff in Kubernetes. 

## Prerequisites

### Docker Pull Secret

In order to pull the Takeoff container you need to have logged into your account which has been given permission to access the Takeoff container in DockerHub. Then if you copy the config.json created by Docker into this directory it will be used to pull the container.

```bash
cp $HOME/.docker/config.json .dockerconfig.json
```

## Installing the Chart

```bash
helm install takeoff-helm . --values values.yaml       
```