from pyray import *
from .scene import Scene
from config import *
from components import singleton, GameState
import ui_components.buttons as button
import ui_components.bars as bar
from minigames import navigate_to
import texture_resources as tex

class PlaygroundScene(Scene):
    map_button: Texture2D

    def load(self):
        self.map_button = load_texture(tex.MAP_BUTTON)

    def render(self):
        clear_background(DARKGRAY)
        button.standard_button(int(SCREEN_WIDTH * 0.20), int(SCREEN_HEIGHT * 0.3), 150, 60, 2, GRAY, BLACK, "Floppy Slime", get_font_default(), lambda: navigate_to(GameState.FLOOPY_BIRD))
        button.multiple_state_button(self.map_button, int(SCREEN_WIDTH * 0.80), int(SCREEN_HEIGHT * 0.75), Scale.DOUBLED, navigate_to_map)

    def unload(self):
        unload_texture(self.map_button)

    def map_view():
        pass

def navigate_to_map():
    singleton.state = GameState.MAP

