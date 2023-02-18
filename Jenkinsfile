pipeline {
    agent any 
    stages {
        stage('Clone') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/VENU-DEVOPS-PROJECTS/building-running-pushing-image-to-docker.git']]])
            }
        }
        stage('listing files') {
            steps {
                sh 'ls -l'
            }
        }
        stage('Docker version') {
            steps {
                sh 'docker --version'
            }
        }
        stage('Building docker image from Dockerfile') {
          steps {
                sh 'docker build -t myclockapp .'
            }
        }
        stage('Tagging image') {
           steps {
               sh 'docker tag myclockapp venuchanapathi1998/binaryclockimage:${BUILD_NUMBER}'
           }
        }
        stage('Pushing to docker hub') {
            steps {
                sh 'docker push venuchanapathi1998/binaryclockimage:${BUILD_NUMBER}'
            }
        }
        stage('Creating the Docker container from the Docker image ceated in previous stage') {
          steps {
                sh ' docker run -d --name clockapp myclockapp'
            }
        }
        stage('cleaning the loaded images') {
            steps {
                sh 'docker stop $(docker ps -aq)'
                sh 'docker rm $(docker ps -aq)'
                sh 'docker rmi $(docker images -q)'
            }
        }
    }
}
