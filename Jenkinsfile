pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh "echo test"
            }
        }
        stage('stage 2') {
            steps {
                script {
                    error "This pipeline stops here!"
                }
            }
        }
    }
}
