from abc import ABC, abstractmethod

class System(ABC):

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def update(self):
        pass    

    @abstractmethod
    def unload(self):
        pass
