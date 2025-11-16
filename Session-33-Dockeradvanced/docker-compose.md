# How to work with Docker Compose

- Basically docker compose will help to run multiple services
- manage shared network and shared volume in structured way

**Steps to execute**

- create folder named docker-comppose, move to that
- create folder named backend and run below commands
```bash
npm init -y
npm install express mysql2
```
- create server.js file and copy code
- created Dockerfile and copy the code

- frontend:
```bash
npm create vite@latest
# select yes
# React
# javascript
# name: frontend
# choose default options by just pressing enter
# ctrl + c for exit
```
- then just create dockerfile under frontend folder

- Last create docker-compose.yml file as shown

```bash
docker compose up -d --build
# you can see image created, network, volume and 3 containers
docker ps
docker logs mysql-container
docker logs backend
docker logs frontend

```
- check localhost:3000
- check localhost:5173

*your all services deployed successfully using docker-compose*
