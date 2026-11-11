from components import GameState
from .minigame import Minigame, navigate_to
from .floopy_bird import FloopyBird

MINIGAMES = {
    GameState.FLOOPY_BIRD: FloopyBird,
}

