import typing
from .game_state import GameState
from .game_data import GameData

class Singleton:
    previous_state: GameState
    state_data: GameData

    def __init__(self):
        self._state = GameState.MENU
        self.previous_state = None
        self.state_data = GameData([])

    @property
    def state(self) -> GameState:
        return self._state

    @state.setter
    def state(self, new_state: GameState):
        if new_state != self._state:
            self.previous_state = self._state
            self._state = new_state

singleton = Singleton()
