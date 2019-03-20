pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh "echo test"
            }
        }
        stage('Build') {
            steps {
                script {
                    error "This pipeline stops here!"
                }
            }
        }
    }
}
