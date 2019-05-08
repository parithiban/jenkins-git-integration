pipeline {
    agent any 
    stages {
        stage('Code Review Notification') { 
            when {
                 allOf {
                    expression { env.CHANGE_ID != null }
                    expression { env.CHANGE_TARGET != null }
                }
                not {
                    anyOf {
                        branch 'development'
                        branch 'master'
                        branch '**upgrade**'
                    }
                }
            }
            steps {
                slackSend channel: '#automation', message: '@here \n CRM Code Review \n Branch - ' + CHANGE_BRANCH + 
                '\n Link - ' + CHANGE_URL
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
