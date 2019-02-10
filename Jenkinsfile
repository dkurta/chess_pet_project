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
                bat "sonar-scanner.bat -D"sonar.projectKey=dkurta_chess_pet_project" -D"sonar.organization=dkurta-github" -D"sonar.sources=."-D"sonar.host.url=https://sonarcloud.io" -D"sonar.login=83e015eb467afd1ccfe234a5f77c5631575bed0b""
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