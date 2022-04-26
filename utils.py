import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECIEVER_EMAIL = os.getenv("RECIEVER_EMAIL")

def send_email(subject, body):
    def send(message):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(SENDER_EMAIL, SENDER_PASSWORD)
        s.sendmail(SENDER_EMAIL, RECIEVER_EMAIL, message.as_string())
        s.quit()
    
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = SENDER_EMAIL
    message["To"] = RECIEVER_EMAIL
    b = MIMEText(body, "html")
    message.attach(b)
    send(message)

def relpath(path):
    return os.path.join(os.path.dirname(__file__), path)