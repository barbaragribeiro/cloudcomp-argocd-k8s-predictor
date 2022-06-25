#### Files

- The ML training code as well as the latest model is under the folder `ml-model`
- The Dockerfile used to build the container, as well as all server code, is under the folder `server`
- The YAML files used by Kubernetes are under the `kubernetes` folder
- The YAML file describing the ArgoCD application is the `manifest.yaml` file
- In order to execute the client script, run:

```bash
sh client.sh <ip:port> <text>
```
