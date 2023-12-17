FROM jenkins/jenkins:lts
USER root
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
ENV JENKINS_HOME /var/jenkins_home
ENV CASC_JENKINS_CONFIG=/var/jenkins_home/casc.yml
COPY jenkins.yml /var/jenkins_home/casc.yml
COPY job_dsl.groovy /var/jenkins_home/job_dsl.groovy
RUN jenkins-plugin-cli --plugins "configuration-as-code:latest" \
    "role-strategy:latest" "groovy:latest" "job-dsl:latest" \
    "ws-cleanup:latest" "dark-theme:latest" "docker-plugin:latest"
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
RUN mv kubectl /usr/local/bin/kubectl