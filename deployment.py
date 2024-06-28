import os
import subprocess

def deploy_application(repo_dir, service_name):
    # Pull the latest changes from the repository
    subprocess.run(["git", "-C", repo_dir, "pull"], check=True)
    print(f"Pulled latest changes in {repo_dir}")
    
    # Restart the application service
    subprocess.run(["systemctl", "restart", service_name], check=True)
    print(f"Restarted service {service_name}")

if __name__ == "__main__":
    repository_directory = "/path/to/repo"
    application_service_name = "your_app_service"
    deploy_application(repository_directory, application_service_name)
