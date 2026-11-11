from .component import Component

class Obstacle(Component):
    is_deadly: bool
    damage: int

    def __init__(self, is_deadly, damage):
        self.is_deadly = is_deadly
        self.damage = damage
