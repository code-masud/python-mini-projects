from .email import Email
import smtplib
from email.message import EmailMessage

class Outlook(Email):

    def create_email(self, receiver, subject, text_body, html_body = None, attachment_path = None) -> EmailMessage:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = receiver
        msg.set_content(text_body)
        if html_body: msg.add_alternative(html_body, subtype='html')
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