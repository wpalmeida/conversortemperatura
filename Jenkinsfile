pipeline {
    agent any
 
    environment {
        // Set Docker Hub credentials ID
        DOCKER_HUB_CREDENTIALS = '5c392039-f8d7-4635-ad5a-e53f7de140f2'
        // Set your Docker image name
        DOCKER_IMAGE_NAME = 'fromjenkins'
    }
 
    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scm
                }
            }
        }
 
        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Build Docker image
                    docker.build("${DOCKER_IMAGE_NAME}:${BUILD_NUMBER}")
                    
                    // Authenticate with Docker Hub
                    docker.withRegistry('https://registry.hub.docker.com', "${DOCKER_HUB_CREDENTIALS}") {
                        // Push Docker image to Docker Hub
                        docker.image("${DOCKER_IMAGE_NAME}:${BUILD_NUMBER}").push()
                    }
                }
            }
        }
    }
}
