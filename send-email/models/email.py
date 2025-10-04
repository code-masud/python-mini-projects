from abc import ABC, abstractmethod
import ssl
from email.message import EmailMessage

class Email(ABC):
    def __init__(self, host, port, sender, password):
        self.host = host
        self.port = port
        self.sender = sender
        self.password = password
        self.context = ssl.create_default_context()

    @abstractmethod
    def create_email(self, receiver, subject, text_body, html_body = None, attachment_path = None) -> EmailMessage:
        pass

    @abstractmethod
    def send_email(self, message: EmailMessage):
        pass

    def __str__(self):
        return f"Sending email using host: {self.host}, port: {self.port}, from: {self.sender}"