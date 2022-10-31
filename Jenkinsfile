pipeline {
    agent any
    stages {
        stage("Testing"){
            agent {
                dockerfile {
                    filename 'Dockerfile.Jenkins'
                }
            }
            steps{
                echo 'testing'
                sh """
		    python manage.py shell
                    python pytest
                    """
            }
        }
        stage('OWASP DependencyCheck') {
			steps {
				dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'Dependency Checker'
			}
		}
    }
    post {
		success {
			dependencyCheckPublisher pattern: 'dependency-check-report.xml'
		}
	}

}
