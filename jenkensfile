pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/Benjaminnworah/vulnerable-python-app.git'
            }
        }

        stage('SAST Scan') {
            steps {
                sh 'bandit -r .'
            }
        }

        stage('Secrets Scan') {
            steps {
                sh 'trufflehog filesystem .'
            }
        }
    }
}
