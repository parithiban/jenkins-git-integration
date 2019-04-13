pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh "echo test"
            }
        }
        stage('Print env') {
            steps {
                sh 'printenv'
            }   
        }
        stage('Print status') {
            steps {
                sh 'git branch'
            }   
        }
    }
}
