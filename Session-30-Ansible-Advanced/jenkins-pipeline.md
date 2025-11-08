# Example of Condition in Pipeline
```groovy
pipeline {
    agent any

    stages {
        stage('build') {
            when { branch 'master'}
            steps {
                echo 'Building code of Master Branch'
            }
        }
        stage('Test') {
            when { branch 'develop'}
            steps {
                echo 'Running all Test cases on develop branch'
            }
        }
    }
}
```