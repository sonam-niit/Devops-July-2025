# Docker commands to understand docker

1. Check docker images
```bash
docker images
```
2. Pull Existing images
```bash
docker pull hello-world
```
3. Run images in container
```bash
docker run hello-world
```
4. See running containers
```bash
docker ps
```
5. To see all containers
```bash
docker ps -a
```
6. to remove containers
```bash
docker rm container-name
```
7. to stop container
```bash
docker stop container-name
```
8. remove all exited containers
```bash
docker container prune -f
```