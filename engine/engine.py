from abc import ABC, abstractmethod

class Engine(ABC):
    def __init__(self):
        super(Engine, self).__init__()

    @abstractmethod
    def needs_service(self):
        pass
