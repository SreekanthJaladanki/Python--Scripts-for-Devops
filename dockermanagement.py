import os
import subprocess

def build_and_run_container(dockerfile_dir, image_name, container_name, ports):
    # Build Docker image
    build_command = ["docker", "build", "-t", image_name, dockerfile_dir]
    subprocess.run(build_command, check=True)
    print(f"Docker image {image_name} built successfully")
    
    # Run Docker container
    run_command = ["docker", "run", "--name", container_name]
    for host_port, container_port in ports.items():
        run_command.extend(["-p", f"{host_port}:{container_port}"])
    run_command.append(image_name)
    subprocess.run(run_command, check=True)
    print(f"Docker container {container_name} is running")

if __name__ == "__main__":
    dockerfile_directory = "/path/to/dockerfile"
    docker_image_name = "my_app_image"
    docker_container_name = "my_app_container"
    port_mappings = {
        8080: 80
    }
    
    build_and_run_container(dockerfile_directory, docker_image_name, docker_container_name, port_mappings)
