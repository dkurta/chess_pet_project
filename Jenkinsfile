pipeline {
    agent any
    stages {
        stage('Greet') {
            steps {
                bat "echo Hello"
            }
        }
        stage('Build Metrics') {
            steps {
                // run bat-script for metrics
                bat "start cmd.exe /C ./scripts/sonarqubeScript.bat"
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
                bat "echo Good Bye!"
            }
        }
    }
}