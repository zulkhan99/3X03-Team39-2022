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

}