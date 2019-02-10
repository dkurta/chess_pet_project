pipeline {
    agent any
    stages {
        stage('Greet') {
            steps {
                bat "./scripts/hello.bat"
            }
        }
        stage('Build Metrics') {
            steps {
                // run bat-script for metrics
                bat "./scripts/sonarqubeScript.bat"
            }
        }
        stage('Deploy') {
            steps {
                // simply call ant command for deployment
                bat "ant"
            }
        }
        stage('Say Good Bye') {
            steps {
                bat "./scripts/hello.bat"
            }
        }
    }
}