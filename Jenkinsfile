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

        }
        stage("Deploying"){

        }
    }
}