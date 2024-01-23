pipeline {
    agent any
 
    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scm
                }
            }
        }
 
        stage('Build') {
            steps {
                script {
                    // Your build commands go here
                    echo "Building the project..."
                }
            }
        }
    }
}
