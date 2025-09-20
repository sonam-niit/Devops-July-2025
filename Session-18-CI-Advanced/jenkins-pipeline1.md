# Setup a Jenkins Pipeline

1. Go to Jenkins Dashboard
2. click on new Item
3. name: SampleJob1
4. select pipeline in type
5. click on OK
6. Description add pipeline description: sample pipeline to understand flow.
7. configure discard old build:
    - Days to keep builds: 5
    - Max # of builds to keep: 10
8. scroll down to script place
9. click on try sample pipeline and click on hello world
10. edit code with below code:
    - stages are like jobs
    - steps are like commands to run
```groovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Check out repository'
            }
        }
        stage('Build') {
            steps {
                echo 'Application build Successfully!'
            }
        }
        stage('Test') {
            steps {
                echo 'All Test Cases passes!'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Application deployed successfully!'
            }
        }
    }
}

```
11. save it and click on build now
12. check console output
13. check stages
14. check pipeline overview
15. to edit again you can click on configure 
