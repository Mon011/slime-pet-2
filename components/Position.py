from .Direction import Direction
from .Component import Component

class Position(Component):
    x: float
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y

# Component.register(Position)