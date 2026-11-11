from pyray import *
from .scene import Scene
from config import *
from components import singleton, GameState
import ui_components.buttons as button
import texture_resources as tex

class MenuScene(Scene):
    BANNER_SCALE = 0.8
    BUTTON_MARGIN = 30

    background: Texture2D
    banner: Texture2D
    play_button: Texture2D
    credits_button: Texture2D
    exit_button: Texture2D

    def load(self):
        self.background = load_texture(tex.MAIN_MENU_BACKGROUND)
        self.banner = load_texture(tex.BANNER)
        self.play_button = load_texture(tex.PLAY_BUTTON)
        self.credits_button = load_texture(tex.CREDITS_BUTTON)
        self.exit_button = load_texture(tex.EXIT_BUTTON)

    def render(self):
        draw_texture_ex(self.background, [0, 0], 0, 1, WHITE)
        draw_texture_ex(self.banner, [SCREEN_WIDTH / 2 - self.banner.width * self.BANNER_SCALE // 2, 0], 0, self.BANNER_SCALE, WHITE)
        button.multiple_state_button(self.play_button, SCREEN_WIDTH // 2 - self.play_button.width // 2, SCREEN_HEIGHT // 2, Scale.DEFAULT, navigate_to_introduction)
        button.multiple_state_button(self.credits_button, SCREEN_WIDTH // 2 - self.credits_button.width // 2, SCREEN_HEIGHT // 2 + self.credits_button.height // 3 + self.BUTTON_MARGIN, Scale.DEFAULT, navigate_to_credits)
        button.multiple_state_button(self.exit_button, SCREEN_WIDTH // 2 - self.exit_button.width // 2, SCREEN_HEIGHT // 2 + self.exit_button.height // 3 * 2 + self.BUTTON_MARGIN * 2, Scale.DEFAULT, exit)
    
    def unload(self):
        unload_texture(self.background)
        unload_texture(self.banner)
        unload_texture(self.play_button)
        unload_texture(self.credits_button)
        unload_texture(self.exit_button)

def navigate_to_introduction():
    singleton.state = GameState.INTRODUCTION

def navigate_to_credits():
    singleton.state = GameState.CREDITS

def exit():
    close_window()
    exit()
    