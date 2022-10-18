pipeline {
    agent any

    stages {
        stage('Docker Compose') {
            steps {
                echo 'Composing'
                step([
                    $class: 'DockerComposeBuilder', 
                    dockerComposeFile: 'docker-compose.yml', 
                    option: [$class: 'StartAllServices'], 
                    useCustomDockerComposeFile: true
                ])
                step([
                    $class: 'DockerComposeBuilder', 
                    dockerComposeFile: 'docker-compose.yml', 
                    option: [
                        $class: 'ExecuteCommandInsideContainer', 
                        command: 'python manage.py collectstatic --no-input --clear', 
                        index: 1, 
                        privilegedMode: true, 
                        service: 'web', 
                        workDir: ''
                    ], 
                    useCustomDockerComposeFile: false])
            }
        }
        stage('Test') {
            steps {
                sh 'docker container ls'
            }
        }
    }
}