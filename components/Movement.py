from .Component import Component
from .Direction import Direction

class Movement(Component):
    speed: float
    direction: Direction
    
    def __init__(self):
        self.speed = 0
        self.direction = Direction.NONE

    def __init__(self, speed, direction):
       self.speed = speed 
       self.direction = direction

# Component.register(Movement)