#!/usr/bin/env python3
import time
import argparse

from src.apps.Jenkins.Infrastructure.ServerJenkinsRepository import ServerJenkinsRepository
from src.apps.Jenkins.Application.Build.JobBuilder import JobBuilder
from src.apps.Jenkins.Application.Find.BuildFinder import BuildFinder
from src.apps.Jenkins.Domain.JobParams import JobParams

parser = argparse.ArgumentParser()

parser.add_argument("-host", "--hostname", help="Jenkins full url i.e: https://your-jenkins-site.com", required=True)
parser.add_argument("-u", "--username", help="Jenkins username", required=True)
parser.add_argument("-tk", "--token", help="Jenkins API token", required=True)
parser.add_argument("-jb", "--jobname", help="Jenkins job name", required=True)
parser.add_argument("-p", "--params", help="Jenkins job parameters", required=False, default="{}")
parser.add_argument("--wait-job", action=argparse.BooleanOptionalAction, help="Wait for the job build status")

args = parser.parse_args()

JENKINS_URL = args.hostname
JENKINS_TOKEN = args.token
JENKINS_USERNAME = args.username
JENKINS_JOB_NAME = args.jobname
JENKINS_JOB_PARAMS = args.params
JENKINS_WAIT_JOB = args.wait_job

# Set Jenkins Connection
repository = ServerJenkinsRepository(url=JENKINS_URL, token=JENKINS_TOKEN, username=JENKINS_USERNAME)

# Build Job
builder = JobBuilder(repository=repository)
builder.exec(name=JENKINS_JOB_NAME, params=JobParams(JENKINS_JOB_PARAMS))

# Get build number
finder = BuildFinder(repository=repository)
build_number = finder.number()
print(f"BUILD NUMBER: {build_number}")

# Set status to executed if JENKINS_WAIT_JOB is not defined
if not JENKINS_WAIT_JOB and build_number:
    print("Job status is : EXECUTED")
    print("::set-output name=job_status::EXECUTED")
    exit(0)

while not (status := finder.exec(build_number)):
    time.sleep(1)

print(f"Job status is : {status}")
print(f"::set-output name=job_status::{status}")

if status != 'SUCCESS':
    exit(1)
