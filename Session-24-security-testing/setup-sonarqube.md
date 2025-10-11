# Setting up sonarqube

- [Download Community Edition](https://www.sonarsource.com/products/sonarqube/downloads/success-download-community-edition/)

- Community Edition is free

- to run sonarqube we need jdk 17 +

- check in your cmd or terminal: java --version

1. once sonar is downloaded extract the same
2. move to that folder and inside bin folder
3. you can see different platform sonar options available
4. if you are windows user just open that location in cmd and run command
5. StartSonar.bat
6. for linux or mac move to its perticular folder and run
7. sonar.sh (run this command)

- you can check in cmd once its started access in browser
- localhost:9000 (SonarQube is Starting)
- then you can see login screen
- default username and password is admin, admin
- it will ask you to reset password, create password which you can remember and 
then you will be redirected to you dashboard screen

**Setup A Project to check security**

- create folder node-project
- move to that folder
- npm init -y (this will create package.json file)
- npm install express (set up dependency)
- create file index.js file

```js
const express = require('express')
const app = express() //server

//api
app.get('/',(req,res)=>{
    res.send('Hello From SonarQube!')
})

//server starting
app.listen(3000,()=>console.log('server started'))
```

- setup sonar-project.properties file for your project

```properties
sonar.projectKey=node-project
sonar.projectName=node-project
sonar.projectVersion=1.0
sonar.sources=.
sonar.exclutions=node_modules/**
sonar.language=js
sonar.sourceEncoding=UTF-8
```

- Setup Sonar Scanner which helps to scan project and feed on Sonar Dashboard
- [Download From Here](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarscanner)
- Extract and set path using environment variable
- open cmd: sonar-scanner -h (if you see output means its working)

- in you project terminal run this command

```bash
sonar-scanner \
-Dsonar.projectBaseDir=%cd% \
-Dsonar.host.url=http://localhost:9000 \
-Dsonar.token=use_token_generated_from_sonar
```

**How to Generate token**

- got to sonar dashboard
- profile icon
- security
- generate token -> user token -> generate -> copy and sace somewhere
- use for scan
- once scan successful then check your dashboard
- refresh and check project and see its passed or failed

- again make some changes in youe code index.js

```js
const express = require('express')
const app = express() //server

//security problems
const dbUser='admin'
const dbPassword='passworrd123'

//api
app.get('/',(req,res)=>{
    res.send('Hello From SonarQube!')
})
//duplicated logics
//Unused Function
function debugLog(msg){
    console.log('DEBUG: ',msg)
}

//server starting
app.listen(3000,()=>console.log('server started'))
```
- run the same command again and check your dashboard
- you can see the security problems and it fails.

