pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'docker build -t flaskwog .'
            }
        }

        stage('Run') {
            steps {
                bat 'docker-compose up -d'
            }
        }

        stage('Test') {
            steps {
                bat 'python e2e.py'
            }
        }

        stage('Finalize') {
            steps {
                bat 'docker-compose down'
            }
        }
    }
}

