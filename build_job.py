#!/usr/bin/env python3
import sys
import time

from src.apps.Jenkins.Infrastructure.ServerJenkinsRepository import ServerJenkinsRepository
from src.apps.Jenkins.Application.Build.JobBuilder import JobBuilder
from src.apps.Jenkins.Application.Find.BuildFinder import BuildFinder
from src.apps.Jenkins.Domain.JobParams import JobParams

def mandatory_arg(argv):
    if argv == "":
        raise ValueError("Required fields: jenkins url, jenkins api token, jenkins username and jenkins job")
    return argv

JENKINS_URL = mandatory_arg(sys.argv[1])
JENKINS_TOKEN = mandatory_arg(sys.argv[2])
JENKINS_USERNAME = mandatory_arg(sys.argv[3])
JENKINS_JOB_NAME = mandatory_arg(sys.argv[4])

#Optional args
JENKINS_JOB_PARAMS = sys.argv[5] if len(sys.argv) > 5 else '{}'

#Set Jenkins Connection
repository = ServerJenkinsRepository(url=JENKINS_URL, token=JENKINS_TOKEN, username=JENKINS_USERNAME)

#Build Job
builder = JobBuilder(repository=repository)
builder.exec(name=JENKINS_JOB_NAME, params=JobParams(JENKINS_JOB_PARAMS))

#Get build number
finder = BuildFinder(repository=repository)
build_number = finder.number()
print(f"BUILD NUMBER: {build_number}")

#Get build status
while not (status := finder.exec(build_number)):
    time.sleep(1)

print(f"Job status is : {status}")
print(f"::set-output name=job_status::{status}")

if status != 'SUCCESS':
    exit(1)