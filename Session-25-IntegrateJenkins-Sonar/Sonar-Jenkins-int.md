# Sonar Jenkins Integartion

- Open your SonarQube folder and start SorarQube
- Access from localhost:9000, login with changed cred.

- open jenkins, start the service
- access localhost:8080 with cred.

- From Jenkins - click on manage jenkins - plugins
- available plugins - search for SonarQube Scanner
- click on install.

- manage jenkins -> system --> Sonar Qube Servers.

![sonarqube Servers](images/sonarqube-servers.png)

- check on environment  variables
- click on Add Sonar
![Step1](images/step1.png)

- you need to add token as secret for that click on add and click on jenkins
![Step2](images/step2.png)
- select secret text
![Step3](images/step3.png)

- generate token from Sonarqube by clicking profile icon -> MyAccount -> change security tab
![Generate token](images/generate-token.png)

- use this token in jenkins
![Step4](images/step4.png)