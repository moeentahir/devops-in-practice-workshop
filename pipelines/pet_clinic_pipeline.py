#!/usr/bin/env python
from gomatic import *
import os, re

print "Updating Meta Pipeline..."

go_server_host = re.search('https?://([a-z0-9.\-._~%]+)', os.environ['GO_SERVER_URL']).group(1)
go_server_url = "%s:%s" % (go_server_host, "8153")
configurator = GoCdConfigurator(HostRestClient(go_server_url))
secret_variables = 'AES:RzT43r0+TsBsR3sPBtYL8g==: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'
pipeline = configurator\
	.ensure_pipeline_group("sample")\
	.ensure_replacement_of_pipeline("PetClinic")\
	.set_git_material(GitMaterial("https://github.com/moeentahir/devops-in-practice-workshop.git", ignore_patterns=set(['pipelines/*']))).ensure_environment_variables({'MAVEN_OPTS': '-Xmx1024m', 'GCLOUD_PROJECT_ID': 'devops-workshop-227508', 'GCLOUD_ZONE': 'us-central1-a', 'GCLOUD_CLUSTER': 'devops-workshop-gke'}).ensure_encrypted_environment_variables({'GCLOUD_SERVICE_KEY': secret_variables})
stage = pipeline.ensure_stage("Commit")
job = stage.ensure_job("build-and-publish").set_elastic_profile_id("docker-jdk")
job.add_task(ExecTask(['./mvnw', 'clean package']))
job.add_task(ExecTask(['bash', '-c', 'docker build --tag pet-app:$GO_PIPELINE_LABEL --build-arg JAR_FILE=target/spring-petclinic-2.0.0.BUILD-SNAPSHOT.jar .']))
job.add_task(ExecTask(['bash', '-c', 'docker login -u _json_key -p"$(echo $GCLOUD_SERVICE_KEY | base64 -d)" https://us.gcr.io']))
job.add_task(ExecTask(['bash', '-c', 'docker tag pet-app:$GO_PIPELINE_LABEL us.gcr.io/$GCLOUD_PROJECT_ID/pet-app:$GO_PIPELINE_LABEL']))
job.add_task(ExecTask(['bash', '-c', 'docker push us.gcr.io/$GCLOUD_PROJECT_ID/pet-app:$GO_PIPELINE_LABEL']))
stage = pipeline.ensure_stage("deploy")
job = stage.ensure_job("deploy")
job.add_task(ExecTask(['bash', '-c', 'echo $GCLOUD_SERVICE_KEY | base64 -d > secret.json && chmod 600 secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud auth activate-service-account --key-file secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud container clusters get-credentials $GCLOUD_CLUSTER --zone $GCLOUD_ZONE --project $GCLOUD_PROJECT_ID']))
job.add_task(ExecTask(['bash', '-c', './deploy.sh']))
job.add_task(ExecTask(['bash', '-c', 'rm secret.json']))

stage = pipeline.ensure_stage("approve-canary")
stage.set_has_manual_approval()
job = stage\
	.ensure_job("complete-canary")\
    .ensure_environment_variables({'GCLOUD_ZONE': 'us-central1-a', 'GCLOUD_PROJECT_ID': 'devops-workshop-227508', 'GCLOUD_CLUSTER': 'devops-workshop-gke'})\
    .ensure_encrypted_environment_variables(secret_variables)
job.set_elastic_profile_id('kubectl')
job.add_task(ExecTask(['bash', '-c', 'echo $GCLOUD_SERVICE_KEY | base64 -d > secret.json && chmod 600 secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud auth activate-service-account --key-file secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud container clusters get-credentials $GCLOUD_CLUSTER --zone $GCLOUD_ZONE --project $GCLOUD_PROJECT_ID']))
job.add_task(ExecTask(['bash', '-c', './complete-canary.sh']))
job.add_task(ExecTask(['bash', '-c', 'rm secret.json']))

configurator.save_updated_config(save_config_locally=True, dry_run=True)
