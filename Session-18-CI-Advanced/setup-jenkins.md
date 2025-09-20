# Setup Jenkins for CI CD pipelines

## Install java

```bash
sudo apt update
sudo apt install fontconfig openjdk-21-jre
java -version
openjdk version "21.0.3" 2024-04-16
OpenJDK Runtime Environment (build 21.0.3+11-Debian-2)
OpenJDK 64-Bit Server VM (build 21.0.3+11-Debian-2, mixed mode, sharing)
```

## Install Jenkins which is with Long term support

```bash
sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update
sudo apt install jenkins
```

## Start Jenkins

1. Enable Jenkins
```bash
sudo systemctl enable jenkins
```
2. Start Jenkins
```bash
sudo systemctl start jenkins
```
3. Check the Status of Jenkins
```bash
sudo systemctl status jenkins
```
- to exit from status you can use ctrl+c shortcut
4. access jenkins dashboard using below link
[Jenkins URL](http://localhost:8080/)
5. unlock using password from this location
```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```
6. After Unlocking, install all the suggested plugins.
7. create first admin user make sure you set up this
8. give values like admin admin easy to remember
9. Confirm Jenkins URL: http://localhost:8080/
10. Continue with Jenkins
