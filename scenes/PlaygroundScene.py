from pyray import *
from .Scene import Scene
from config import *
from pathlib import Path
from components import singleton, GameState
import ui_components.buttons as button
import ui_components.bars as bar
from enum import Enum

class PlaygroundScene(Scene):
    map_button: Texture2D

    def load(self):
        self.map_button = load_texture(str(Path("assets/buttons/map-button.png")))

    def render(self):
        clear_background(DARKGRAY)
        button.standard_button(int(SCREEN_WIDTH * 0.20), int(SCREEN_HEIGHT * 0.3), 150, 60, 2, GRAY, BLACK, "Floppy Slime", get_font_default(), lambda: navigate_to_game(Minigame.FLOOPY_BIRD))
        button.multiple_state_button(self.map_button, int(SCREEN_WIDTH * 0.80), int(SCREEN_HEIGHT * 0.75), Scale.DOUBLED, navigate_to_map)

    def unload(self):
        unload_texture(self.map_button)

    def map_view():
        pass

class Minigame(Enum):
    FLOOPY_BIRD = 0

def navigate_to_map():
    singleton.state = GameState.MAP

def navigate_to_game(game: Minigame):
    if(game == Minigame.FLOOPY_BIRD):
        singleton.state = GameState.FLOOPY_BIRD
