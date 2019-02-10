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
                withAnt(installation: 'ant1.10.5') {
                    //call ant
                    bat "ant"
                }
            }
        }
    }
}