pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                //
            }
        }
        stage('Test') {
            steps {
                //
            }
        }
        stage('Deploy') {
            steps {
                withAnt(installation: 'ant1.10.5') {
                    //call ant
                    bat "ant build"
                }
            }
        }
    }
}