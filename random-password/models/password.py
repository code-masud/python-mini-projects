from .base import Base
import string
import random

class Password(Base):
    
    def generate(self):
        if self.length < 8:
            raise ValueError("Password length must be grater then 8")
        else:
            characters = string.ascii_letters + string.digits + string.punctuation
            result = "".join(random.choice(characters) for i in range(self.length))
            return result