# Docker Volume 

- Docker container is not having any persistent volume
- once container stopped or deleted data lost.
- to manage the data after deleting the container as well you can use docker volume

```bash
docker volume --help
docker volume create myvolume
docker volume ls

docker run -d --name myapp -v myvolume:/usr/share/nginx/html -p 8081:80 nginx
docker exec -it myapp bash
echo "<h1>Hello From Docker Volume</h1>" > /usr/share/nginx/html/index.html
exit
# check in browser localhost:8081
docker rm -f myapp
docker run -d --name myapp -v myvolume:/usr/share/nginx/html -p 8081:80 nginx
# again check localhost:8081 
# data persist in volume and beause of that you can see same data
docker inspec myapp # you can see mounting details

```

### Bind Mounts

- Bind mounts diretcly maps your local system folder into container
- whatever changes on host -> instant changes in container
- whatever container writes --> appears on host
- perfect for development

```bash
cd ~
mkdir myapp
echo "Hello from Host Machine" > myapp/index.html
docker run -d --name myapp -v ~/myapp:/usr/share/nginx/html -p 8081:80 nginx
# check in browser localhost:8081
# your container must access your host file directly
```