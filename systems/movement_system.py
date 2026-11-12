import math
from .system import System
from components import *
from components.direction import Direction

class MovementSystem(System):
    DIAGONAL = math.sqrt(0.5)
    DIRECTION_VECTORS = {
        Direction.NONE: (0, 0),
        Direction.TOP: (0, -1),
        Direction.TOP_RIGHT: (DIAGONAL, -DIAGONAL),
        Direction.RIGHT: (1, 0),
        Direction.BOTTOM_RIGHT: (DIAGONAL, DIAGONAL),
        Direction.BOTTOM: (0, 1),
        Direction.BOTTOM_LEFT: (-DIAGONAL, DIAGONAL),
        Direction.LEFT: (-1, 0),
        Direction.TOP_LEFT: (-DIAGONAL, -DIAGONAL),
    }

    def load(self):
        pass

    def update(self):
        for entity in singleton.state_data.entities:
            movement = entity.get_component(Movement)
            position = entity.get_component(Position)
            if movement is None or position is None:
                continue

            dx, dy = self.DIRECTION_VECTORS[movement.direction]
            position.x += dx * movement.speed
            position.y += dy * movement.speed

    def unload(self):
        pass
