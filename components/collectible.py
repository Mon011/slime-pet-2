from .component import Component

class Collectible(Component):
    on_collect: callable

    def __init__(self, on_collect):
        self.on_collect = on_collect
