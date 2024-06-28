import requests

def get_jenkins_job_status(jenkins_url, job_name, jenkins_user, jenkins_token):
    url = f"{jenkins_url}/job/{job_name}/lastBuild/api/json"
    response = requests.get(url, auth=(jenkins_user, jenkins_token))
    
    if response.status_code == 200:
        build_info = response.json()
        status = build_info['result']
        print(f"Latest build status for job {job_name}: {status}")
    else:
        print(f"Failed to get status for job {job_name}, status code: {response.status_code}, response: {response.text}")

if __name__ == "__main__":
    jenkins_url = "http://your-jenkins-url"
    job_name = "your-job-name"
    jenkins_user = "your-username"
    jenkins_token = "your-api-token"
    
    get_jenkins_job_status(jenkins_url, job_name, jenkins_user, jenkins_token)
