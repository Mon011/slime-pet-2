from components import *
from minigames import Minigame, MINIGAMES
from .system import System

class EntityGeneratorSystem(System):
    minigame: Minigame

    def __init__(self):
        self.minigame = None

    def load(self):
        pass

    def update(self):
        self._update_minigame()

    def unload(self):
        self._switch_minigame(None)

    def _update_minigame(self):
        minigame_class = MINIGAMES.get(singleton.state)
        current_class = type(self.minigame) if self.minigame is not None else None
        if minigame_class is not current_class:
            self._switch_minigame(minigame_class)

        if self.minigame is not None:
            self.minigame.update()

    def _switch_minigame(self, minigame_class: type):
        if self.minigame is not None:
            self.minigame.stop()
        self.minigame = minigame_class() if minigame_class is not None else None
        if self.minigame is not None:
            self.minigame.start()
