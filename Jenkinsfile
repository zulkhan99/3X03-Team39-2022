pipeline {
    agent any

    stages {
		stage('Build') {
		    steps {
			    sh 'echo "building..."'
		    }
		}
        stage("Testing"){
            steps{
                sh '''#!/bin/bash
		        echo "hello world"
                '''
            }
        }
        stage("Deploying"){
            steps{
                echo 'deploying'
                sh 'python3 manage.py runserver'
            }
        }
    }
}