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
                //simply call ant command for deployment
                bat "ant"
            }
        }
    }
}