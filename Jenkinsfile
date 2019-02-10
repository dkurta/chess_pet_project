pipeline {
    agent any
    stages {
        stage('Greet') {
            steps {
                bat "echo greetings"
            }
        }
        stage('Deploy') {
            steps {
                bat "ant"
            }
        }
    }
}