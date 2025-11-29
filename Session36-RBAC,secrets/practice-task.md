# MYSQL Deployment with Secrets

- Secret -> store MYSQL username and password, root password
- Deployment -> Run MYSQL image using Secrets
- Service -> Expose MYSQL inside Cluster (type: cluster IP)
- MYSQL Client Pod --> to test connection (temp)

*Implementation Hint*

- create secrets
- kubectl get secrets
- describe them --> kubect describe secret secret-name

- deployment file using secret
- kubectl apply -f deployment-mysql.yml
- create service.yml
- kubectl apply -f service-mysql.yml

**Test Connection - temp pod**

```bash
kubectl run mysql-client --image=mysql -it --rm -- /bin/bash
mysql -h mysql -u admin -p
# Enter password
# check you are connected or not and ctrl+c

```

### Verify Env variable inside MYSQL Container 

- how we did in prev example
- get all environment variable in one command