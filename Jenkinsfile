pipeline {
    agent any
    stages {
        stage('Greet') {
            steps {
                bat "echo Hello"
            }
        }
        stage('Deploy') {
            steps {
                //simply call ant command for deployment
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