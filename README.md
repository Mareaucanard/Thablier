# Thablier
Epitech 2023-2024 Whanos
This project aims at automatically deploying an application into a cluster, every time a push is done in the repository.

Whanos uses these technologies :
 - Docker : To enable testing without being dependent of the parent OS
 - GitHub Actions : To automate the testing of projects
 - Jenkins : To start jobs and deploy containers to test various languages
 - Ansible : To automate the deployment of Whanos
 - Kubernetes : To manage the differents testing environments

Whanos can provide repository testing for different languages :
 - C
 - Java
 - JavaScript
 - Python
 - Befunge

***

## Dependencies
 - Docker
 - Docker compose
 - Kubectl

## Deployment
Make sure that BuildImage.sh is executable (so `chmod +x jenkins/BuildImage.sh` from the root of the repository) <br>
Then run it ! (`./jenkins/BuildImage.sh`)

Once the build phase is complete, you must set a new environment variable named `ADMIN_USER_PASSWORD`. <br>
This will be the admin account password for the Jenkins platform. (This variable must be set before every start/deployments of Whanos)

Then, you can start Whanos with<br>
`docker compose --file jenkins/DockerCompose.yml up -d`<br>
from the root of the repository.

Now you can access your Jenkins interface on localhost over the port 8080! (you can set it to another port by editing L.7 in the DockerCompose.yml)