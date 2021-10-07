#!/usr/bin/env python3
import sys
import time
import jenkins
import json
import requests
import urllib3
import json

# Arguments
optional_arg = lambda argv, index, default: default if (len(argv) <= index or argv == "") else argv[index]
if len(sys.argv) < 4:
    raise ValueError("Required fields: jenkins url, jenkins api token, jenkins username and jenkins job")

JENKINS_URL = sys.argv[1]
JENKINS_TOKEN = sys.argv[2]
JENKINS_USERNAME = sys.argv[3]
JENKINS_JOB_NAME = sys.argv[4]
JENKINS_JOB_PARAMS = optional_arg(sys.argv, 5, '{}')
JENKINS_WAIT_JOB = optional_arg(sys.argv, 6, "wait")

# Setup Jenkins Connection and start build
connection = jenkins.Jenkins(JENKINS_URL, JENKINS_USERNAME, JENKINS_TOKEN)
queue_id = connection.build_job(JENKINS_JOB_NAME, parameters=json.loads(JENKINS_JOB_PARAMS), token=JENKINS_TOKEN)
print(f"Build queued with queue_id: {queue_id}")

# Wait for the build to start and store the build no
protocol, domain = JENKINS_URL.split("://")
build_number = None
build_url = None
while True:
    try: 
        queue_info = requests.get(f"{protocol}://{JENKINS_USERNAME}:{JENKINS_TOKEN}@{domain}/queue/item/{queue_id}/api/json?pretty=true").json()
        build_number = queue_info["executable"]["number"]
        raw_url = queue_info["executable"]["url"]
        build_protocol, build_url = raw_url.split("://")

        break
    except KeyError:
        # todo: sometimes executable is in queue_info, but
        # number is not, why?
        if "executable" in queue_info:
            print(queue_info["executable"])
        time.sleep(3)

if build_number is None:
    raise Exception("Build could not be started")

print(f"Build started with build_number: {build_number}")
print(f"::set-output name=job_build_number::{build_number}")
print(f"Build URL: http://{build_url}")

# early exit?
if JENKINS_WAIT_JOB == "no-wait" and build_number:
    print(f"Build completed with status: EXECUTED")    
    print("::set-output name=job_status::EXECUTED")
    exit(0)

# Wait for the build to complete
console_lines = 0
build_info = None
while True:
    console = connection.get_build_console_output(JENKINS_JOB_NAME, build_number).splitlines()
    for i in range(console_lines, len(console)):
        print(console[i])
    console_lines = len(console)
    build_info = connection.get_build_info(JENKINS_JOB_NAME, number=build_number)
    if (status := build_info["result"]):
        break

    time.sleep(3)

# Summary
print(f"Build completed with status: {status}")
print(f"::set-output name=job_status::{status}")

if status not in ['SUCCESS', 'UNSTABLE']:
    exit(1)