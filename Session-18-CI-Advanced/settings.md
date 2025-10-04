# Setting up maven tools

1. settings icon
2. tools
3. go to maven installtion --> name it like "my maven"
4. select maven version 
5. add installer like apache

- this will configure Maven from tools as well.

# To use this tool in your pipeline use below in your script
```groovy
pipeline {
    agent any
    tools {
        maven 'my maven' // Name from Global Tool Configuration
    }
    stages {
        stage('Check java Version') {
            steps {
                echo 'Check java Version'
                sh 'java -version'
                
                sh 'mvn -version'
            }
        }
    }
}

```
- so now this will your maven from configured tools not from the default settings of your system.

# To Setup direct maven project not pipeline

1. setting icon
2. plugins -> available plugins --> search maven integration
3. install

# create new Item as Maven project

1. new Item
2. give name --> select Maven project
3. select git and add repo and branch name
4. in goals type for clean install
5. This will also build your project.


