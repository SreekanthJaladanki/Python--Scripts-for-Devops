import requests
import time
import smtplib
from email.mime.text import MIMEText

def send_alert(subject, body, to_email):
    from_email = "your_email@example.com"
    from_password = "your_email_password"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP_SSL('smtp.example.com', 465) as server:
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, msg.as_string())

def check_service_health(url, alert_email):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"Service at {url} is up")
        else:
            send_alert("Service Down", f"The service at {url} returned status code {response.status_code}", alert_email)
            print(f"Service at {url} is down, status code {response.status_code}")
    except requests.RequestException as e:
        send_alert("Service Down", f"The service at {url} is not reachable: {e}", alert_email)
        print(f"Service at {url} is not reachable: {e}")

if __name__ == "__main__":
    service_url = "http://example.com/health"
    alert_email = "alert@example.com"
    check_interval = 60  # seconds

    while True:
        check_service_health(service_url, alert_email)
        time.sleep(check_interval)
