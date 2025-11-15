# run command for docker

- docker run image-name
- this will run image in a container by giving any unique name without giving any port any extra configurations
- It is running in forground so you can see output there in terminal

- docker run --name myapplication -d -p 8081:80 docker/getting-started

- --name is used to give container name
- -d for detached (to run in background)
- -p for port number
- first port is host port(system port)
- second port is docker internal port (like what is req by your app)

- means internally it will use port 80 but to access in browser use localhost:8081

- now check runnin containers: docker ps (see the status of container)
- if you want to stop your container: docker stop myapplication
- once its stoped it won't reflect in running conatainers
- docker ps -a (here you can see that container is exited)
- now remove it: docker rm myapplication

- usaully its a good practice to stop and remove container
- if you want to do direct remove you can do forcefully: docker rm name -f

## From where docker downloads images

- from official docker repository
- from where you can get details of images? 
[Docker hub Link](https://hub.docker.com/)

- check mysql image details
- [Link for Mysql](https://hub.docker.com/_/mysql)

```bash
docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=123456 -d mysql
# if image not available locally it will pull from repo
# -e for environment variable
docker ps # check container is up or not
# now how to connect with DB , access inside container
docker exec -it mysql-container bash
mysql -u root -p # enter password 123456
# now you are inside mysql cli
```
```sql
show databases;
create database pw;
create table student (id int, name varchar(20));
insert into student (id,name) values (1,'Alex');
select * from student;
exit; -- exit from mysql
```
```bash
exit # exit from container
```

## Troubleshoot with containers

```bash
# check logs
docker logs mysql-container
```