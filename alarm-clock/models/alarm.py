from abc import ABC, abstractmethod

class Alarm(ABC):
    def __init__(self):
        self.alarms = []
        self.triggered_alarms = set()

    @abstractmethod
    def add_alarm(self):
        pass

    @abstractmethod
    def check_alarm(self):
        pass

    def ring_alarm(self, alarm_time):
        pass
    