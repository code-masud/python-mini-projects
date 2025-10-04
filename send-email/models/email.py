from abc import ABC, abstractmethod
import ssl

class Email(ABC):
    def __init__(self, host, port, sender, password):
        self.host = host
        self.port = port
        self.sender = sender
        self.password = password
        self.context = ssl.create_default_context()

    @abstractmethod
    def create_email(self):
        pass

    @abstractmethod
    def send_email(self):
        pass

    def __str__(self):
        return f"Sending email using host: {self.host}, port: {self.port}, from: {self.sender}"