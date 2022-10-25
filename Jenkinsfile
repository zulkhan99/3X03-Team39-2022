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
        stage('OWASP DependencyCheck') {
			steps {
				dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'Default'
			}
		}
    }

}