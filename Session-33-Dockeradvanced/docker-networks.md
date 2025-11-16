# How containers can communicate

- If container wants to communicate with each other that they must run under common network

## How to create network?

```bash
docker network --help # to see command details
docker network ls # to list available networks
docker network create sonam
# let's create 2 containers
docker run --name app1 --network=sonam -d -p 8081:80 nginx
docker run --name app2 --network=sonam -d -p 8082:80 nginx

# to check connectivity
docker exec -it app1 sh
curl http://app2 # you can code of nginx default page
exit

# same you can check for app2 to app1 as well
# try without using network and it won't work
# if you just wanted to check connection use busybox simple image
docker run --name app1 --network=sonam it busybox
#open another terminal
docker run --name app2 --network=sonam it busybox
# now check using ping connand
ping app1
```