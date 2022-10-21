pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile.Jenkins'
        }
    }

    stages {
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