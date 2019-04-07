from abc import ABC

class Constriant(ABC):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    @abstractmethod
    def check():
        return