# Takeoff Helm Chart

This is our example template of a Helm chart for deploying Takeoff in Kubernetes. 

# TODO

- Add data injection documentation 
- Provide the license key

## Prerequisites


### Fill out License key of takeoff

In values.yaml you need to provide license key. you can leave the takeoff_access_token blank for now
# Secrets passed to the Takeoff container as environment variables
# Here you need to add your own access token and license key.
secrets:
  TAKEOFF_ACCESS_TOKEN: ""
  LICENSE_KEY: ""



## Launching

To install the helm chart you need to first create a namespace. ex. 
```
kubectl create namespace takeoffsearch 
```


To install the helm chart ensure you have the desired values in the `values.yaml` file and the config set in the `takeoff-config.yaml` (initial launch config for Takeoff). Then run the following command:

```bash
helm install takeoffsearch ./ --namespace takeoffsearch --values values.yaml      
```

This should spin up takeoff search project in your Kubernetes cluster.


## Post installation

Once we have takeoffsearch helm chart installed, we can check if the search app is running using portforward. What I usually do is just to portforward the rag service to localhost:8000. And we can login using the following username and password: 


## Data Injection 