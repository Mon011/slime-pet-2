from .component import Component 

class Gravity(Component):
    g: float 

    def __init__(self, g: float = 1.0):
        self.g = g