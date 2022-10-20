pipeline {
    agent {
        docker {
            filename 'Dockerfile.Jenkins'
        }
    }

    stages {
		// stage('Build') {
		//     steps {
		// 	    echo 'building'
		//     }
		// }
        stage("Testing"){
            steps{
                sh 'echo xd'
                sh 'echo test'
            }
        }
        stage("Deploying"){
            steps{
                echo 'deploying'

            }
        }
    }
}