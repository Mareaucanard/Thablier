#!/bin/bash
# To be executed in parent directory
# Starts Jenkins in a Docker container

# Check if local image exists

if [[ "$(docker images -q jenkins:local 2> /dev/null)" == "" ]]; then
    echo "Jenkins image not found. Building..."
    docker build -t jenkins:local -f jenkins/Dockerfile .
fi

# Create a container if it doesn't exist

if [ ! "$(docker ps -q -f name=jenkins)" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=jenkins)" ]; then
        # cleanup
        docker rm jenkins
    fi
    # run your container
    docker run --rm -d -p 8080:8080 -p 50000:50000 \
    --env CASC_JENKINS_CONFIG=/var/jenkins_home/casc.yml \
    --volume /home/epi/WhanOS/jenkins/jenkins.yml:/var/jenkins_home/casc.yml \
    --volume /home/epi/WhanOS/jenkins/job_dsl.groovy:/var/jenkins_home/job_dsl.groovy \
    --name jenkins jenkins:local
fi