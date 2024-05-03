# Takeoff Helm Chart

This is our example template of a Helm chart for deploying Takeoff in Kubernetes. 

# TODO

- Add data injection documentation 
- Remove unused yaml: namespace, data-pvc and deployment 
- Try install from scratch again
- change takeoff-pro to takeoff and then they don't need to login to takeoffusers

## Prerequisites

### Docker Pull Secret

In order to pull the Takeoff container you need to have logged into your account which has been given permission to access the Takeoff container in DockerHub. Then if you copy the config.json created by Docker into this directory it will be used to pull the container.

```bash
cp $HOME/.docker/config.json .dockerconfig.json
```

## Launching

To install the helm chart ensure you have the desired values in the `values.yaml` file and the config set in the `takeoff-config.yaml` (initial launch config for Takeoff). Then run the following command:

```bash
helm install takeoff-helm . --values values.yaml       
```

This should spin up Takeoff in your Kubernetes cluster.
