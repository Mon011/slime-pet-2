from abc import ABC, abstractmethod
from components import singleton, GameState
from entities import Entity
from enum import Enum

class Minigame(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def update(self):
        pass

    def stop(self):
        singleton.state_data.entities.clear()

    def add_entity(self, entity: Entity):
        singleton.state_data.entities.append(entity)

def navigate_to(game_state: GameState):
    singleton.state = game_state

