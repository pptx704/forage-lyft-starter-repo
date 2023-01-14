from abc import ABC, abstractmethod

class Serviceable(ABC):
    def __init__(self):
        super(Serviceable, self).__init__()

    @abstractmethod
    def needs_service(self):
        pass
