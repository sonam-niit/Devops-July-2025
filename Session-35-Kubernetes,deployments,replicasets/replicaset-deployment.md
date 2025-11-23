# Pods, replicasets & Deployment

1. Pods:

    - a pod is smallest deployable unit in K8s.
    - Inside a pod we can run single or multi containers
    - pod run containers, but they cannot restart if they fails

```bash
# create pod.yml file
kubectl apply -f pod.yml
kubectl get pods
kubectl describe pod pod-name
kubectl delete pod pod-name
```
2. Replicaset

    - It is a specifing numbers of replicas which are running all the times
    - in case any replica pod fails then it will recreate in replicaset
    - Let's create replicaset
    - create a file named: replicaset.yml (use shown code here)
    
```bash
kubectl apply -f replicaset.yml # take ynl from official doc
kubectl get rs
kubectl get pods # created 3 pods
kubectl describe replicaset frontend
# try to take any of pod name and check pod details
kubectl describe pod pod-name
# let's delete pod by our own to check replicaset create new pod or not
kubectl delete pod pod-name
kubectl get pods # you can see new pod created due to replicaset
# Incase if you wnat to scale
kubectl scale replicaset frontend --replicas=5
kubectl scale replicaset frontend --replicas=2
kubectl delete replicaset frontend
```
3. Deployment

    - It provides all controller updates and the rollback features
    - rollout, and rollback you can do, versions you can update
    - also it provides fetaures of replicaset as well
    - let's create one file deployment.yml

```bash
 kubectl apply -f nginx-deployment.yml
 kubectl get deployments
 kubectl get rs # internally it includes rs

 kubectl get pods # 3 pods running
 kubectl get pods --show-labels # pods with labels

 kubectl describe deployment nginx-deployment
 # you can try deleting pod and it will recrease
 # Saclling possible
 kubectl scale deployment nginx-deployment --replicas=5
 kubectl scale deployment nginx-deployment --replicas=2

 # update image version for deployment
 kubectl set image deployment/nginx-deployment nginx=nginx:1.16.1
 
 # Check Rollout status
 kubectl rollout status deployment/nginx-deployment
  kubectl describe deployment
 # rollback (undo)
 kubectl rollout undo deployment/nginx-deployment
 kubectl rollout history deployment/nginx-deployment

 kubectl delete deployment nginx-deployment

```
## For Rollout you can also edit yml file as well
- create file as mentioned here 
- then run apply command
- see deployment status, num of pods
- then edit the file with version as well as annotation cause message
- again run apply command and check history.