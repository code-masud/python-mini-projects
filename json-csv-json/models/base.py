from abc import ABC, abstractmethod

class Base(ABC):
    def __init__(self, path_from, path_to):
        self.path_from = path_from
        self.path_to = path_to

    def convert(self):
        pass