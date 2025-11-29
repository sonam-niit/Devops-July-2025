# What is Secrets in kubernetes?

- A Secret is a kubernetes Object that stores sensitive info:
- like password, tokens, API keys, Certificates, SSH keys

## Let's create secret

```bash
# Empty Secret
kubectl create secret generic empty-secret
kubectl get secret empty-secret

# Secret with credentials
kubectl create secret generic my-secret \
--from-literal=username=admin \
--from-literal=password=Pass@123

kubectl get secret my-secret
```

### Create Secret from YML file

```yml
apiVersion: v1
kind: Secret
metadata:
  name: pod-secret
type: Opaque
data:
  username: YWRtaW4=
  password: UGFzc0AxMjM=
```
- here I have used username: admin and password: Pass@123 and 
- here its mentioned base64 value

```bash
echo -n "admin" | base64
echo -n "Pass@123" | base64
```
```yml
apiVersion: v1
kind: Pod
metadata:
  name: secret-demo
spec:
  containers:
    - name: app
      image: nginx
      env:
        - name: USERNAME 
          valueFrom: 
            secretKeyRef:
              name: pod-secret
              key: username
        - name: PASSWORD 
          valueFrom: 
            secretKeyRef:
              name: pod-secret
              key: password
```

- inside pod I am using Secret values by passing as env variable
- to verify go inside the pod

```bash
kubectl exec -it secret-demo -- /bin/bash
echo $USERNAME
echo $PASSWORD
# if you are able to see original value means we are able to access secrets
```
