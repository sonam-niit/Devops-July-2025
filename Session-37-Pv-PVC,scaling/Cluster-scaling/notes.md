# Kubernetes cluster scaling

- EKS Cluster 

- make sure aws cli is configured in your system
- install eksctl to work with EKS Cluster

```bash
aws sts get-caller-identity # if cli configured then you can see your acc details

# for ARM systems, set ARCH to: `arm64`, `armv6` or `armv7`
ARCH=amd64
PLATFORM=$(uname -s)_$ARCH

curl -sLO "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_$PLATFORM.tar.gz"

# (Optional) Verify checksum
curl -sL "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_checksums.txt" | grep $PLATFORM | sha256sum --check

tar -xzf eksctl_$PLATFORM.tar.gz -C /tmp && rm eksctl_$PLATFORM.tar.gz

sudo install -m 0755 /tmp/eksctl /usr/local/bin && rm /tmp/eksctl

eksctl version
```
[Reference Link](https://docs.aws.amazon.com/eks/latest/eksctl/installation.html)

### Setup a cluster

```bash
eksctl create cluster --name dev-cluster --region us-east-1 --nodegroup-name dev-nodes --node-type t3.medium --nodes 2 --nodes-min 2 --nodes-max 5 --managed
```
- meaning 
    --name: name of your cluster
    --region: region AWS
    --node-type: EC2 instance type
    --nodes: number of instance in node group
    --managed: managed node group

- To update Kube Configuration
- tell your system to communicate with EKS cluster not minikube

```bash
aws eks --region us-east-1 update-kubeconfig --name dev-cluster
# run below command to execute on eks cluster
kubectl get nodes
kubectl get svc

# Deploy application
kubectl create deployment nginx --image=nginx
# create service
kubectl expose deployment nginx --port=80 --type=LoadBalancer

kubectl get svc
# see external IP generated with load balancer service
# copy that and paste in browser so you can access default nginx page

kubectl logs deployment/nginx

kubectl delete service nginx
kubectl delete deployment nginx

# Delete cluster
eksctl delete cluster --name dev-cluster --region us-east-1
```

## Scaling


```bash
kubectl create deployment nginx --image=nginx --replicas=4
kubectl get pods
kubectl get pods -o wide
# when you see detailed description you can see may be 4 pods running on diffrent nodes

kuebctl delete deployment nginx
```

*Dynamic Scaling we will implement with more AWS Services working sessions*