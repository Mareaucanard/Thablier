FROM jenkins/jenkins:lts
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
ENV JENKINS_HOME /var/jenkins_home
RUN jenkins-plugin-cli --plugins "configuration-as-code:latest" \
    "role-strategy:latest" "groovy:latest" "job-dsl:latest" "ws-cleanup:latest"
COPY jenkins.yml /var/jenkins_home/casc.yml
COPY job_dsl.groovy /var/jenkins_home/job_dsl.groovy
ENV CASC_JENKINS_CONFIG=/var/jenkins_home/casc.yml