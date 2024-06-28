import subprocess

def renew_ssl_certificates():
    # Renew SSL certificates using Certbot
    renew_command = ["certbot", "renew", "--quiet"]
    subprocess.run(renew_command, check=True)
    print("SSL certificates renewed successfully")

if __name__ == "__main__":
    renew_ssl_certificates()
