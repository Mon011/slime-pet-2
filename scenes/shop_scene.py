from pyray import *
from .scene import Scene
from config import *
from components import singleton, GameState
from entities import slime
import ui_components.buttons as button
import ui_components.bars as bar
import texture_resources as tex

class ShopScene(Scene):
    background: Texture2D
    map_button: Texture2D
    health_bar_logo: Texture2D
    hunger_bar_logo: Texture2D
    progress_bar_texture: Texture2D
    money_bar_texture: Texture2D

    def load(self):
        self.background = load_texture(tex.SHOP_BACKGROUND)
        self.map_button = load_texture(tex.MAP_BUTTON)
        self.health_bar_logo = load_texture(tex.HEALTH_BAR_LOGO)
        self.hunger_bar_logo = load_texture(tex.HUNGER_BAR_LOGO)
        self.progress_bar_texture = load_texture_from_image(bar.progress_bar_image)
        self.money_bar_texture = load_texture(tex.MONEY_BAR)

    def render(self):
        clear_background(WHITE)
        draw_texture_ex(self.background, [0, 0], 0, Scale.QUADRUPLED, WHITE) #TODO: Change background with proper scaling
        button.multiple_state_button(self.map_button, int(SCREEN_WIDTH * 0.80), int(SCREEN_HEIGHT * 0.75), Scale.DOUBLED, navigate_to_map)
        bar.value_bar(self.money_bar_texture, str(slime.coins), int(SCREEN_WIDTH * 0.82), int(SCREEN_HEIGHT * 0.05), self.money_bar_texture.width * 3 // 2)

    def unload(self):
        unload_texture(self.background)
        unload_texture(self.map_button)
        unload_texture(self.health_bar_logo)
        unload_texture(self.hunger_bar_logo)
        unload_texture(self.progress_bar_texture)
        unload_texture(self.money_bar_texture)

def navigate_to_map():
    singleton.state = GameState.MAP