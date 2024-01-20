pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'sim_api'
        VIRTUAL_ENV = 'sim_api_env'
        CONTAINER_NAME = 'sim_api_cont'
    }

    stages {
        stage('Setup') {
            steps {
                script {
                    // Set up any necessary environment configurations
                    sh "python -m venv ${VIRTUAL_ENV}"
                    sh "source ${VIRTUAL_ENV}/Scripts/activate"
                }
            }
        }

        stage('Lint Check') {
            steps {
                script {
                    // Perform linting (replace with your linting command)
                    sh "flake8 app/"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh "docker build -t ${DOCKER_IMAGE_NAME} ."
                }
            }
        }

        stage('Deploy to Container') {
            steps {
                script {
                    // Run Docker container (replace with your container run command)
                    sh "docker run -d -p 8090:80 --name ${CONTAINER_NAME} ${DOCKER_IMAGE_NAME}"
                }
            }
        }
    }

    post {
        success {
            script {
                echo 'Lint check passed, Docker image built, and application deployed to a container successfully!'
            }
        }
        failure {
            script {
                echo 'Lint check failed, Docker image build or deployment to a container aborted.'
            }
        }
    }
}