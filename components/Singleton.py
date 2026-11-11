import typing
from .GameState import GameState
from .GameData import GameData

class Singleton:

    state: GameState
    state_data: GameData

    def __init__(self):
        self.state = GameState.MENU
        self.state_data = GameData([])

singleton = Singleton()