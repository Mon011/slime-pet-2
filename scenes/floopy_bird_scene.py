from pyray import *
from .scene import Scene
from entities import Entity
import ui_components.buttons as button
from components import singleton, GameState
from config import *

class FloopyBirdScene(Scene):
    slime_sprite_image: Image
    slime_sprite: Texture2D

    def load(self):
        pass

    def render(self):
        clear_background(BLUE)

    def unload(self):
        pass
