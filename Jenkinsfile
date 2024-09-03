pipeline {
    agent any
    environment {
        SERVER_NAME = "192.168.1.9"  // Updated Nexus server name
        DOCKER_DEV_REPO = "docker-dev.192.168.1.9:443"  // Nexus Docker repository with port 443
        DOCKER_IMAGE = "my-docker-image"
        DOCKER_TAG = "${BUILD_NUMBER}"  // Use Jenkins build number as the tag
        NEXUS_REPOSITORY = "docker-hosted"
    }
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }
        stage('Push Docker Image to Nexus') {
            steps {
                script {
                    // Tagging the Docker image with the correct Nexus repository URL
                    sh "docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_DEV_REPO}/${NEXUS_REPOSITORY}/${DOCKER_IMAGE}:${DOCKER_TAG}"
                    // Pushing the Docker image to Nexus
                    sh "docker push ${DOCKER_DEV_REPO}/${NEXUS_REPOSITORY}/${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
            }
        }
    }
}
