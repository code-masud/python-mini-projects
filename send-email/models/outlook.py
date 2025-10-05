import os
import mimetypes
import smtplib
from email.message import EmailMessage
from .email import Email

class Outlook(Email):

    def create_message(self, receiver: str, subject: str, text_body: str, html_body: str = None, attachment_path: str = None) -> EmailMessage:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = receiver
        msg.set_content(text_body)

        if html_body:
            msg.add_alternative(html_body, subtype='html')

        if attachment_path:
            if os.path.exists(attachment_path):
                mime_type, encoding = mimetypes.guess_type(attachment_path)
                maintype, subtype = mime_type.split("/")
                with open(attachment_path, 'rb') as file:
                    msg.add_attachment(file.read(), maintype=maintype, subtype=subtype, filename=os.path.basename(attachment_path))
            else:
                raise FileNotFoundError(f"Attachment not found: {attachment_path}")
        return msg

    def send_email(self, message: EmailMessage):
        print(f"{super().__str__()}")
        print("Please wait...")
        try:
            with smtplib.SMTP(self.host, self.port) as server:
                server.starttls(context = self.context)
                server.login(self.sender, self.password)
                server.send_message(message)
            print("Email send successfully")
        except Exception as e:
            print(f"An error occurred while sending email: {e}")