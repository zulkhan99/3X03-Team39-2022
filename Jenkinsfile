pipeline {
    agent any

    stages {
        stage("Building"){
            agent{
                docker{
                    image 'python'
                }
            }
            steps{
                sh '-m venv env'
                sh 'source env/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage("Testing"){
            steps{
                echo 'testing'
                sh 'pytest'
            }
        }


    }
    post {
		always {
			echo 'The pipeline completed'
		}
		success {				
			echo "Django Application Up and running!!"
		}
		failure {
			echo 'Build stage failed'
			error('Stopping early…')
		}
	}
}