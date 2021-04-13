# Build jenkins job from Github Action :rocket:

This action builds a jenkins job with parameters. (Single Job)

## Inputs

### `jenkins-token`
https://www.jenkins.io/blog/2018/07/02/new-api-token-system/
**(Required)**
 
### `jenkins-url`
**i.e** https://your-jenkins-site.com
**(Required)** 

### `jenkins-user`
user owner of the token
**(Required)** 

### `jenkins-job`
Jenkins job name

**i.e** Production-deployment-pipeline
**(Required)** 

### `job-params`

**Not mandatory**

Set jenkins params as JSON string:  

**i.e**
```
 "{'param1': 'value1', 'param2': 'value2'}"
``` 


## Outputs

###  `status/result`

* FAILURE
* SUCCESS
* ABORTED


## Example usage
```
    - name: Build single job
      uses: Mondtic/build-jenkins-job@master
      with:
        jenkins-url: ${{ secrets.JENKINS_URL }}
        jenkins-token: ${{ secrets.JENKINS_TOKEN }}
        jenkins-user: ${{ secrets.JENKINS_USER }}
        jenkins-job: ${{ secrets.JENKINS_JOB }}
        jenkins-job-params: "{'stringparam': 'stringvalue', 'booleanparam': false}"
```
