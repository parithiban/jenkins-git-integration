pipeline {
    agent any 
    stages {
        stage('Code Review Notification') { 
            when {
                not {
                    anyOf {
                        branch "development"
                        branch "master"
                    }
                }
            }
            steps {
                slackSend channel: '#automation', message: 'Code Review -  <' + CHANGE_URL + '|' + CHANGE_BRANCH + '>'
            }
        }
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
