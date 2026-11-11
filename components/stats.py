from .component import Component

class Stats(Component):
    health: int
    damage: int
    defence: int

    def __init__(self, health, damage, defence):
        self.health = health
        self.damage = damage
        self.defence = defence