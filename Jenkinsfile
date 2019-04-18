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
                slackSend color:'#5cb85c', channel: '#automation', message: '😎 CRM Build Success  - #' + BUILD_NUMBER + ' - "' + BRANCH_NAME + '" (<' + BUILD_URL + '|Open>)'
            }   
        }
    }
}
