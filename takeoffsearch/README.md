# Takeoff Search Helm Chart

This is our example template of a Helm chart for deploying Takeoff Search app in Kubernetes. 

# TODO

- Complete the data injection documentation.
- Provide the license key information.

## Prerequisites

### License Key Configuration

You must provide a license key in the `values.yaml` file. Leave the `takeoff_access_token` field empty for now. The secrets configuration below is where you will input your access token and license key, which are passed to the Takeoff container as environment variables:

```yaml
secrets:
  TAKEOFF_ACCESS_TOKEN: ""
  LICENSE_KEY: ""
```

## Launching

### Creating a Namespace

Start by creating a Kubernetes namespace for the deployment:

```bash
kubectl create namespace takeoffsearch 
```

### Installing the Helm Chart

Ensure you have configured the `values.yaml` and `takeoff-config.yaml` files with the appropriate settings for your deployment. Use the following command to install the Helm chart:

```bash
helm install takeoffsearch ./ --namespace takeoffsearch --values values.yaml
```

This command deploys the Takeoff search project into your Kubernetes cluster.

## Post-Installation

### Verifying the Application

After installing the Takeoffsearch Helm chart, you can verify if the search application is operational by forwarding the service port to your local machine:

```bash
kubectl port-forward service/takeoffsearch 8000:80 --namespace takeoffsearch
```

Open a web browser and navigate to `http://localhost:8000` to access the Takeoff search interface. Log in with the provided credentials.

- username: macquarie
- password: macquarie2024


### Data Injection


TODO