# Docker Core Components

1. Docker imagges: Read only blue-print of application
    - which contains os libraries, dependencies, code, configuration
    - eg. python, node:20 , nginx:latest
    - download it as template and just use it

2. Docker Containers:
    - A running instance of image
    - image: Template (blue print)
    - container: running 
    
## How to start working with docker

### Let's install Docker in Linux / ubuntu

[Reference Link](https://docs.docker.com/engine/install/ubuntu/)

```bash
# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update

sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Check Status
sudo systemctl status docker

# if its not running then run below command
sudo systemctl start docker

```
## Install Docker in Mac

```bash
brew update
brew install --cask docker
```

- If you don't want install like this than the another option is you can install docker desktop
- which is very easy to download, install and use.

*Once installed check version*

- docker --version
- docker version (if engine is running you can see both client and server details)
