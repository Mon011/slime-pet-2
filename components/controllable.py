from .component import Component

class Controllable(Component):
    up: bool
    down: bool
    left: bool
    right: bool
    jump: bool

    def __init__(self, up, down, left, right, jump):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.jump = jump