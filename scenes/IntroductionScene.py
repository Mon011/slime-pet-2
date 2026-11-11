from pyray import *
from .Scene import Scene
from config import *
from components import singleton, GameState
import ui_components.buttons as button
from entities import slime
from pathlib import Path

class IntroductionScene(Scene):
    slime_sprite_image: Image
    slime_sprite: Texture2D
    next_button_bounds: Rectangle

    def load(self):
        self.slime_sprite_image = load_image(str(Path("assets/entities/slime/static/sprite-main.png")))
        self.slime_sprite = load_texture_from_image(self.slime_sprite_image)
        self.next_button_bounds = Rectangle(int(SCREEN_WIDTH * 0.75), int(SCREEN_WIDTH / 2) - self.slime_sprite.width, 150,60)
        unload_image(self.slime_sprite_image)

    def render(self):
        clear_background(BLUE)
        draw_text("This is your new Slime!", int(SCREEN_WIDTH / 2) - 150, int(SCREEN_HEIGHT / 8), 27, BLACK)
        draw_texture_ex(self.slime_sprite, [int(SCREEN_WIDTH / 2) - self.slime_sprite.width, int(SCREEN_HEIGHT / 2)], 0, 2, WHITE)
        draw_text("Your slime pet's name: " + slime.name, int(SCREEN_WIDTH / 2) - self.slime_sprite.width - 150, int(SCREEN_HEIGHT * 0.80), 36, WHITE)
        button.standard_button(int(SCREEN_WIDTH * 0.75), int(SCREEN_WIDTH / 2) - self.slime_sprite.width, 150, 60, 2, GRAY, BLACK, "NEXT", get_font_default(), navigate_to_park)

    def unload(self):
        pass
    
def navigate_to_park():
    singleton.state = GameState.PARK
