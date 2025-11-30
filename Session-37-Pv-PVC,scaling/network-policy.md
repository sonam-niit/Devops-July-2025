# What are network Policies in K8s

- Network Policy controls which pods can talk to which pods at the network level.

- They work like firewall rules for pods
- they control

    1. Ingress: incomig traffic to pod
    2. egress: outgoing trafiic from a pod

- without network policy (by default) all traffic is allowed (everything can talk to everything)

- with network policy --> default become DENY

## To apply network policy with minikube

- minikube start --cni=calico

- frontend (label: app=frontend)
- backend (label: app=backend)
- We want: Only frontedn pod should be able to access backend pod
- Everything else should be blocked