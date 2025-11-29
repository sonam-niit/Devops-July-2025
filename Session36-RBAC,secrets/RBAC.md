# role Based Access Control

- manage permission from different users and services

## Create Service account: service-account.yml

```yml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: dev-user
```

```bash
kubectl apply -f service-account.yml
kubectl get sa
# Let's Check Permission
kubectl auth can-i get pods --as=system:serviceaccount:default:dev-user
kubectl auth can-i get secrets --as=system:serviceaccount:default:dev-user
# you can see no 
```
### Create Role: role.yml

```yml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: dev-user
rules:
- apiGroups: [""] # "" indicates the core API group
  resources: ["pods","secrets"]
  verbs: ["get", "watch", "list"]
```

```bash
kubectl apply -f role.yml
kubetl get role
```

### Create role-binding.yml

```yml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: dev-user-binding
  namespace: default
subjects:
- kind: ServiceAccount
  name: dev-user
  namespace: default
roleRef:
  kind: Role 
  name: dev-user 
  apiGroup: rbac.authorization.k8s.io
```

```bash
kubectl apply -f role-binding.yml
kubectl get rolebinding

# now again check permissions
kubectl auth can-i get pods --as=system:serviceaccount:default:dev-user
kubectl auth can-i get secrets --as=system:serviceaccount:default:dev-user
kubectl auth can-i list pods --as=system:serviceaccount:default:dev-user
kubectl auth can-i list secrets --as=system:serviceaccount:default:dev-user
```

### Clean up resources

```bash
kubectl delete rolebinding dev-user-binding
kubectl delete role dev-user
kubectl delete sa dev-user
```