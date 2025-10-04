from abc import ABC, abstractmethod

class Base:
    def __init__(self, length):
        self.length = length

    @abstractmethod
    def generate(self):
        pass