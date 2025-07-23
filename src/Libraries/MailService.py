
# --//[ESSENTIAL IMPORTS]\\--
from dotenv import load_dotenv
import os

# --//[LIBRARY IMPORTS]\\--
from Libraries.Templates import get_email_template
import Libraries.TerminalService as tservice
from email.message import EmailMessage
import smtplib

# --//[MAIL SERVICE CLASS]\\--
class MailService:
    def __init__(self):
        # --//[LOAD ENVIRONMENT VARIABLES]\\--
        load_dotenv()
        self.smtp_server = os.getenv("SMTP_SERVER")
        self.smtp_port = int(os.getenv("SMTP_PORT"))
        self.smtp_user = os.getenv("SMTP_USER")
        self.smtp_password = os.getenv("SMTP_PASSWORD")
        self.linkedin_profile_link = os.getenv("LINKEDIN_PROFILE_LINK")
        
        # --//[CHECK ENVIRONMENT VARIABLES]\\--
        if not all([self.smtp_server, self.smtp_port, self.smtp_user, self.smtp_password]):
            raise ValueError("SMTP configuration is not set in the environment variables.")

    # --//[SEND HTML EMAIL]\\--
    def send_html_email(self, to_address, subject, html_content):
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.smtp_user
        msg['To'] = to_address
        msg.set_content(html_content, subtype='html')
        

        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
            server.login(self.smtp_user, self.smtp_password)
            server.send_message(msg)
    
    # --//[SENDING EMAIL TO CONTACTS]\\--
    def send_email_to_contacts(self, contacts: list, status_index: int):
        """
        Sends an email to each contact in the list with the specified status.
        
        :param contacts: List of contacts to send emails to.
        :param status_index: Status index of the email to be sent.
        """

        variant = 0
        for contact in contacts:
            # --//[CHECK IF CONTACT CAN RECEIVE EMAIL]\\--
            can_send, email_status = contact.getStatus() # status 0 = sending first email, 1 = sending second email, 2 = sending third email

            if can_send and email_status == status_index:
                subject, body = get_email_template(
                    status_index=status_index,
                    contact=contact,
                    variant=variant,
                    sender_name=self.smtp_user,
                    discovery_method="Hier wird später ein KI Text stehen",
                    linkedin_profile_link=self.linkedin_profile_link
                )

                try:
                    self.send_html_email(contact.Email, subject, body)
                    print(f"Email sent to {contact.name()} at {contact.Email}")
                except Exception as e:
                    print(f"Failed to send email to {contact.name()} at {contact.Email}: {e}")

                variant = (variant + 1) % 5
        
        tservice.emptyLine()
        tservice.header("EMAILS SENT")
        tservice.emptyLine()