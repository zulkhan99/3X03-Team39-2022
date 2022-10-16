pipeline{
    agent {
        docker {
            image 'python:3:10-alpine'
        }
    }
    stages{
        stage('Build server'){
            steps{
                sh 'python manage.py runserver'
            }
        }
    }
}