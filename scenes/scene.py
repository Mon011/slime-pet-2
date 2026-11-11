from abc import ABC, abstractmethod

class Scene(ABC):
    
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def unload(self):
        pass
