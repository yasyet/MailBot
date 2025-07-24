# --//[ESSENTIAL IMPORTS]\\--
from time import sleep
from dotenv import load_dotenv
import os

# --//[LIBRARY IMPORTS]\\--
import Libraries.FileService as fservice
import Libraries.Templates as templates
import Libraries.TerminalService as tservice
from email.message import EmailMessage
from email.header import Header
from email.utils import formataddr
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
        self.mail_name = os.getenv("MAIL_NAME")
        self.linkedin_profile_link = os.getenv("LINKEDIN_PROFILE_LINK")
        
        # --//[CHECK ENVIRONMENT VARIABLES]\\--
        if not all([self.smtp_server, self.smtp_port, self.smtp_user, self.smtp_password]):
            raise ValueError("SMTP configuration is not set in the environment variables.")

    # --//[SEND HTML EMAIL]\\--
    def send_html_email(self, to_address, subject, html_content):
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['To'] = to_address
        msg['From'] = self.smtp_user

        msg.set_content(html_content, subtype='html', charset='utf-8')

        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
            server.login(self.smtp_user, self.smtp_password)
            server.send_message(msg)
    
    # --//[SENDING EMAIL TO CONTACTS]\\--
    def send_email_to_contacts(self, contacts: list, status_index: int) -> list:
        """
        Sends an email to each contact in the list with the specified status.
        
        :param contacts: List of contacts to send emails to.
        :param status_index: Status index of the email to be sent.

        :return: List of contacts that were successfully emailed.
        If no contacts were emailed, returns None.
        """

        variant = 0
        changed_contacts = []
        for contact in contacts:
            # --//[CHECK IF CONTACT CAN RECEIVE EMAIL]\\--
            can_send, email_status = contact.getStatus() # status 0 = sending first email, 1 = sending second email, 2 = sending third email

            if can_send and email_status == status_index:
                subject, body = templates.get_email_template(
                    status_index=status_index,
                    contact=contact,
                    variant=variant,
                    sender_name=self.mail_name,
                    discovery_method="Hier wird später ein KI Text stehen",
                    linkedin_profile_link=self.linkedin_profile_link
                )

                try:
                    self.send_html_email(contact.Email, subject, body)
                    print(f"Email sent to {contact.name()} at {contact.Email}")
                    changed_contacts.append(contact) # Add contact to changed contacts list
                except Exception as e:
                    print(f"Failed to send email to {contact.name()} at {contact.Email}: {e}")

                variant = (variant + 1) % 5
                sleep(1.5)
            else:
                sleep(0.1)
        
        # --//[IF CHANGED CONTACTS EXIST]\\--
        if changed_contacts:
            for contact in changed_contacts:
                contact.setStatus(status_index + 1)  # Increment status index for each contact

            tservice.emptyLine()
            tservice.header("EMAILS SENT AND CONTACTS UPDATED")
            tservice.emptyLine()

            return changed_contacts
        # --//[IF NO CONTACTS WERE CHANGED]\\--
        else:
            tservice.emptyLine()
            tservice.header("NO EMAILS SENT")
            tservice.emptyLine()

            return None