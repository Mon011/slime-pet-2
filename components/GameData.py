from entities import Entity

class GameData():
    entities: list[Entity]

    def __init__(self, entities):
        self.entities = entities
        
