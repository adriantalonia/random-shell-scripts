# Kubernetes commands

### Status of different K8s components
```sh
kubectl get nodes | pod | services | replicaset | deployment
```

### Get Pods IP address
```sh
kubectl get pod -o wide
```

### CRUD of deployment
```sh
kubectl create | edit | delete deployment [name]
```

### Debugging pods and services
```sh
kubectl logs [pod name] # get logs
kubectl describe pod [pod name] # get additional information of a pod
kubectl describe service [service name] # get additional information of a pod
```

### Get Interactive Terminal on a POD
```sh
kubectl exec -it [pod name] -- /bin/bash
```

### Use configuration file for CRUD
```sh
kubectl apply -f [file-name.yaml] # Create / Update
kubectl delete -f [file-name.yaml] # Delete
```
