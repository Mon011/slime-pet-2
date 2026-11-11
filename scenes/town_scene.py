from pyray import *
from .scene import Scene
from config import *
from components import singleton, GameState
from entities import slime
import ui_components.buttons as button
import ui_components.bars as bar
import texture_resources as tex

class TownScene(Scene):
    background: Texture2D
    park_button: Texture2D
    map_button: Texture2D
    health_bar_logo: Texture2D
    hunger_bar_logo: Texture2D
    progress_bar_texture: Texture2D
    main_sprite_texture: Texture2D

    def load(self):
        self.background = load_texture(tex.TOWN_BACKGROUND)
        self.park_button = load_texture(tex.PARK_BUTTON)
        self.map_button = load_texture(tex.MAP_BUTTON)
        self.health_bar_logo = load_texture(tex.HEALTH_BAR_LOGO)
        self.hunger_bar_logo = load_texture(tex.HUNGER_BAR_LOGO)
        self.progress_bar_texture = load_texture_from_image(bar.progress_bar_image)
        self.main_sprite_texture = load_texture(tex.SLIME_SPRITE)

    def render(self):
        clear_background(WHITE)
        draw_texture_ex(self.background, [0, 0], 0, Scale.QUADRUPLED, WHITE) #TODO: Change background with proper scaling
        button.multiple_state_button(self.park_button, int(SCREEN_WIDTH / 10), int(SCREEN_HEIGHT * 0.75), Scale.DOUBLED, navigate_to_park)
        button.multiple_state_button(self.map_button, int(SCREEN_WIDTH * 0.80), int(SCREEN_HEIGHT * 0.75), Scale.DOUBLED, navigate_to_map)
        bar.progress_bar(self.progress_bar_texture, self.health_bar_logo, int(SCREEN_WIDTH * 0.65), int(SCREEN_HEIGHT * 0.05), slime.healthpoints, 100, RED)
        bar.progress_bar(self.progress_bar_texture, self.hunger_bar_logo, int(SCREEN_WIDTH * 0.65), int(SCREEN_HEIGHT * 0.13), slime.hunger, 100, RED)
        draw_texture_ex(self.main_sprite_texture, [SCREEN_WIDTH / 2 - self.main_sprite_texture.width * Scale.QUADRUPLED / 2, int(SCREEN_HEIGHT * 0.75)], 0, Scale.QUADRUPLED, WHITE)

    def unload(self):
        unload_texture(self.background)
        unload_texture(self.park_button)
        unload_texture(self.map_button)
        unload_texture(self.health_bar_logo)
        unload_texture(self.hunger_bar_logo)
        unload_texture(self.progress_bar_texture)
        unload_texture(self.main_sprite_texture)

def navigate_to_park():
    singleton.state = GameState.PARK

def navigate_to_map():
    singleton.state = GameState.MAP
    
