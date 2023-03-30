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
		bat 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
		bat 'docker push manor513/worldofgames-app:latest'
            }
        }
    }
}
