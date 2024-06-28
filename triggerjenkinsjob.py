import requests

def trigger_jenkins_job(jenkins_url, job_name, jenkins_user, jenkins_token):
    url = f"{jenkins_url}/job/{job_name}/build"
    response = requests.post(url, auth=(jenkins_user, jenkins_token))
    
    if response.status_code == 201:
        print(f"Successfully triggered job {job_name}")
    else:
        print(f"Failed to trigger job {job_name}, status code: {response.status_code}, response: {response.text}")

if __name__ == "__main__":
    jenkins_url = "http://your-jenkins-url"
    job_name = "your-job-name"
    jenkins_user = "your-username"
    jenkins_token = "your-api-token"
    
    trigger_jenkins_job(jenkins_url, job_name, jenkins_user, jenkins_token)
