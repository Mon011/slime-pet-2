from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities import Entity

class GameData():
    entities: list[Entity]

    def __init__(self, entities):
        self.entities = entities
        
