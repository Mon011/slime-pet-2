from .direction import Direction
from .component import Component

class Position(Component):
    x: float
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y
