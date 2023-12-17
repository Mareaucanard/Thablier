#!/bin/bash
# To be executed in parent directory
# Builds custom Jenkins image for the WhanOS project.

docker build -t someone2love/jenkins_whanos:latest -f jenkins/Dockerfile jenkins/
