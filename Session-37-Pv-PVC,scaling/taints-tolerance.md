# What is Taint?

- A Taint is applied to a node and it repels pods that do not have a maching tolerance

- Effects For taints

1. NoSchedule: Pod will not schedule on that node
2. PreferNoSchedule: Kubernetes tries to avoid that node
3. NoExecute: Pod is evicted if running + new Pod won't schedule

**How to apply taint?**

```bash
kubectl taint nodes minikube app=backend:NoSchedule
# Means only the pod with tolerance for app=backend can run on node1
```

- after applying taint try creating pod directly
```bash
kubectl run nginx --image=nginx
#Check
kubectl describe pod nginx
# you can see pod scheudling is failed due to taint
```
# What is Tolerance?

- Tolerance is added to your pod, so the pod is allowed to run on tainted node.
- toleration-pod.yml
```yml
apiVersion: v1
kind: Pod
metadata:
  name: tolerated-pod
spec:
  containers:
  - name: nginx
    image: nginx
  tolerations:
  - key: "app"
    operator: "Equal"
    value: "backend"
    effect: "NoSchedule"
```
- means above yml file created pod can run on tainted node with above mentioned command.

```bash
kubectl apply -f toleration-pod.yml
kubectl describe pod tolerated-pod
# you can see this pod is scheduled and running beacuse of toleration
```
### Remove Taint

```bash
kubectl taint nodes minikube app=backend:NoSchedule-
# - symbol indicating to remove taint
# once it is remove check 
kubectl get pods
# you can nginx pod got scheduled and running
```

