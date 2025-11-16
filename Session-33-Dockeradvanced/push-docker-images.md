# Push Docker Images to Docker Hub

- Create account on Docker Hub: [DockerHub](https://hub.docker.com/)

- Once account created successfully
- go to wsl or your terminal and execute below command

```bash
docker login
# enter username
# enter password #password is not visible just type and enter
#  you can see login succeded
# incase if it ask for device registration 
# open given link in browser and type given code in shell
# device will get registered.
```
## Push Image to docker hub

```bash
# go to your node app created yesterday
docker build -t mynodeapp .
docker images # check created image

docker tag mynodeapp:latest sonamsoni/mynodeapp:v1
# mynodeapp:latest its local image name
# sonamsoni/mynodeapp:v1 --> sonamsoni is my username
# mynodeapp is the name i want to give for my image
# v1 is the version, you can give number as well

docker push sonamsoni/mynodeapp:v1
# once pushed check in browser docker hub
```