# volumes in Kubernetes

- Volumes in Kubernetes is directory which is accessible to containers in a Pod.
- It is used to store and share data beyond the lifecycle of container process.

## Volume types:

1. Empty Dir: temp storage shared by containers in a Pod

2. hostPath: Mount a file/directory from the host node

3. PVC (persistence volume claim): Bind a presistence volume for durable storage

4. configMaps/Secret: mount configurations map or secret

### Example of Empty Dir Volume

- create empty-dir.yml as shown here

```bash
kubectl apply -f empty-dir.yml
kubectl get pods
kubectl describe pod shared-volume-pod # you can see 2 containers running

kubectl logs shared-volume-pod -c reader # -c container name
```
- In this example its one shared volume is accessible by all the containers running under same pod.
- in this case when you delete the pod data will be lost. If container crash or restart then data remains there.

### How to persist Volume

- PV - which remains there after deleting the pod as well (storage/disk space provided by admin/dynamically)

- PVC - persistence Volume Claim - a req povided  by user for storage

**When to use**

- to persist data even if pod delete
- to decouple storage from pod
- to enable dynamic provision of storage

- Pod --> PVC --> PV --> Storage (Disk Space)

- Pod uses PVC, PVC binds PV, PV connects to the actual Physical or cloud space

- create pv.yml, pvc.yml, pod.yml

```bash
kubectl apply -f pv.yml
kubectl apply -f pvc.yml
kubectl apply -f pod.yml

kubectl get pods
kubectl describe pod pvc-demo-pod
kubectl exec pvc-demo-pod -- cat /data/test.txt

## Let's delete pod
kubectl delete pod pvc-demo-pod
## Let's create reader-pod to read volume data
kubectl apply -f reader-pod.yml
kubectl get pods
kubectl logs pvc-reader-pod

## Clean up Resources
kubectl delete pod pvc-reader-pod
kubectl delete pvc my-pvc
kubectl delete pv my-pv
```