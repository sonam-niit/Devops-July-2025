# Helm Chart ?

- It is a Package format which is used by Helm, which is package manager for Kubernetes.

- just like apt install packages on ubuntu and Yum for Linux, Helm install application on kubernetes in repetable, version-controlled and templatized way.

- without helm you need to create files manually like
    - deployment.yml
    - service.yml
    - pvc.yml
    - ingress.yml
    - configmaps.yml
    - secrets.yml
- all these files can be managed by helm..

## How to use helm?

- install Helm first using below mentioned link
[Reference Link](https://helm.sh/docs/intro/install/)

- Donwload and install as per your OS.

- For ubuntu
```bash
sudo snap install helm --classic
helm version
# Create helm chart
helm create myapp
# once your chart is ready
# Keep chart.yaml, values.yaml, deployment.yaml, service.yaml, _helpers.tpl

# edit values.yaml, deployment.yaml, service.yaml as shown here
helm install myapp ./myapp/ --debug
# these will create all services, deployments based on config
kubectl get deployment
kubectl get pods
kubectl get svc

# to remove them
helm uninstall myapp
```
