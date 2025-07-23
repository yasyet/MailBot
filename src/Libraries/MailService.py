
# --//[ESSENTIAL IMPORTS]\\--
from dotenv import load_dotenv
import os


# --//[LIBRARY IMPORTS]\\--
from email.message import EmailMessage
#from pathlib import Path
import smtplib

# --//[MAIL SERVICE CLASS]\\--
class MailService:
    def __init__(self):
        load_dotenv()
        self.smtp_server = os.getenv("SMTP_SERVER")
        self.smtp_port = int(os.getenv("SMTP_PORT"))
        self.smtp_user = os.getenv("SMTP_USER")
        self.smtp_password = os.getenv("SMTP_PASSWORD")

    def send_html_email(self, to_address, subject, html_content):
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.smtp_user
        msg['To'] = to_address
        msg.set_content(html_content, subtype='html')

        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
            server.login(self.smtp_user, self.smtp_password)
            server.send_message(msg)
        