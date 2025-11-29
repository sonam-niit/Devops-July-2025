# Services in kubernetes

- Service gives pods a stable IP and DNS name for app to talk with them.

**Why we need services?**

- Pods have dynamic IPs
- Replicas of a pod exists behind the deployment
- Clients should not care about replicas or pod restart or scaling
- load balancing across pod replicas

*Use services for those pods*

- find right pods via selectors
- sends traffic across via load balancers
- provides a stable cluster IP or External IP

## Types of Services

1. Cluster IP
    - expose service inside cluster only
    - cannot reach from outside
    - Use Case: Backend Microservice connecting with each other
    - eg. user-service, payment-service, db-service

2. NodePort:
    - opens port on every node between (30000-32700)
    - access them externally: NodeIP:NodePort
    - Use Case: quick testing

3. Load Balancer:
    - works on cloud providers
    - create external cloud load balancer
    - expose the service to the internet
    - Usecase: Web App, APIs

4. ExternalName:
    - maps a service to a DNS name outside cluster
    - no proxying just use CNAME
    - Use Case: External DB (AWS RDS)

## Example

1. create deployment.yml
2. create service.yml

```bash
kubectl apply -f deployment.yml
kubectl get deployment
kubectl get pods
kubectl apply -f service.yml
kubectl get svc

minikube service my-service
# access localhost:given ip in broswer to see nginx default page
```

### Change Type from NodePort to LoadBalancer

```bash
kubectl delete service my-service
kubectl apply -f service.yml
kubectl get svc
# external Ip will show pending due to Minikube cluster
# in cloud you can take externalId:port to access it in browser
# here again use
minikube service my-service
```

### Use ClusterIP

- type: ClusterIP 
- that service is accessible from one pod to another internally
- if you create one another pod in that you use curl command with localhost:port its accessible