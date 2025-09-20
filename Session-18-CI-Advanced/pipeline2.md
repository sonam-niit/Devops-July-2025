# Create Jenkins Pipeline to check Java Version

1. cretae new Item
2. select pipeline
3. set description and other settings
4. write script
```groovy
pipeline {
    agent any

    stages {
        stage('Check java Version') {
            steps {
                echo 'Check java Version'
                sh 'java --version'
            }
        }
    }
}

```
5. Build Now and check output in console.