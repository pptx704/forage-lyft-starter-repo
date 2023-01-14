from abc import ABC, abstractmethod

class Tire(ABC):
    def __init__(self, ):
        super(Tire, self).__init__()

    @abstractmethod
    def needs_service(self):
        pass