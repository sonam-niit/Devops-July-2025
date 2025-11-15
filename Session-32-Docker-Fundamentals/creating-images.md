# Creating Images with Docker

- For your perticular project if you want to create docker image
- you need to set Dockerfile
- file name must be Dockerfile
- its not having any kind of extention

- in this file we need to set some configurations like what os, what dependency, how to run application, what port required to expose.

## Basic components to write in Dockerfile

1. FROM: Base Image (starting point)
2. WORKDIR: set working directory inside container
3. COPY: COPY your code from host to container
4. RUN: Execute commands while building image
5. CMD: Default command when container starts
6. ENV: set environment variables
7. ENTRYPOINT: Main command that always runs
8. EXPOSE: inform container which port listens

### Let's Create one Node app Image

- create folder node-app
- move to that folder: cd node-app
- npm init -y
- npm i express 
- create file named: index.js
- add below mentioned code
```js
const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send("Hello from Express!");
});

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});

```
- create Dockerfile
- add below code
```dockerfile
# Use Base Image
FROM node:22-alpine 
# Set working directory inside a container
WORKDIR /app
#Copy package.json first (for caching)
COPY package.json .
# install Dependency
RUN npm install
# copy rest code files
COPY . .
# Expose application Port
EXPOSE 3000
# Command to run application
CMD ["node", "index.js"]
```
### Let's Build Image

```bash
docker build -t mynodeapp .
# build to build an image
# -t target name 
# mynodeapp is name of my image
# . indicates location of docker file which is root location

# Once image build you can check images
docker images 
# now let's run this image in container
docker run --name nodeapp -d -p 3000:3000 mynodeapp

docker ps

docker logs nodeapp # to see logs of container

# access application using localhost:3000 in browser
```
**Congratulation you deployed your node application in container**
