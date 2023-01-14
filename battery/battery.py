from abc import ABC, abstractmethod

class Battery(ABC):
    def __init__(self, ):
        super(Battery, self).__init__()

    @abstractmethod
    def needs_service(self):
        pass