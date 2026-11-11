from pyray import *
from .scene import Scene
from config import *
from components import singleton, GameState
import ui_components.buttons as button
import texture_resources as tex

class CreditsScene(Scene):
    BANNER_SCALE = 0.8
    BUTTON_WIDTH = 250
    BUTTON_HEIGHT = 80
    BUTTON_MARGIN = 30

    background_image: Image 
    background: Texture2D
    banner_image: Image
    banner: Texture2D
    back_button: Texture2D

    def load(self):
        self.background_image = load_image(tex.MAIN_MENU_BACKGROUND)
        self.background = load_texture_from_image(self.background_image)
        self.banner_image = load_image(tex.BANNER)
        self.banner = load_texture_from_image(self.banner_image)
        self.back_button = load_texture(tex.BACK_BUTTON)

        unload_image(self.background_image)
        unload_image(self.banner_image)

    def render(self):
        clear_background(WHITE)
        draw_texture_ex(self.background, [0, 0], 0, 1, WHITE)
        draw_texture_ex(self.banner, [SCREEN_WIDTH / 2 - self.banner.width * self.BANNER_SCALE / 2, 0], 0, self.BANNER_SCALE, WHITE)
        text = "PRODUCTION:\nMon011 PROGRAMMING\nJanDomanMI PROGRAMMING\nmxdevPL DESIGN\nKlecekman DESIGN"
        font_size = 35
        text_width = measure_text(text, font_size)
        x = (get_screen_width() - text_width ) // 2
        y = (get_screen_height() - font_size) // 2
        draw_text(text,x,y-50,font_size,BLACK)
        button.multiple_state_button(self.back_button, SCREEN_WIDTH // 2 - self.back_button.width * 2, SCREEN_HEIGHT // 2 + self.back_button.height * 4, Scale.QUADRUPLED, navigate_to_menu)

    def unload(self):
        unload_texture(self.back_button)

def navigate_to_menu():
    singleton.state = GameState.MENU
    