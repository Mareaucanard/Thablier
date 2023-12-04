#!/bin/bash
# To be executed in parent directory
# Builds custom Jenkins image for the WhanOS project.

docker build -t jenkins:local -f jenkins/Dockerfile jenkins/