from pyray import *
from .scene import Scene
from config import *
from components import singleton, GameState
from minigames import navigate_to
import ui_components.buttons as button

class GameOverScene(Scene):
    TITLE = "GAME OVER"
    TITLE_FONT_SIZE = 80
    BUTTON_WIDTH = 200
    BUTTON_HEIGHT = 60
    BUTTON_MARGIN = 40

    def load(self):
        pass

    def render(self):
        clear_background(BLACK)

        title_width = measure_text(self.TITLE, self.TITLE_FONT_SIZE)
        draw_text(self.TITLE, (SCREEN_WIDTH - title_width) // 2, int(SCREEN_HEIGHT * 0.3), self.TITLE_FONT_SIZE, RED)

        buttons_width = self.BUTTON_WIDTH * 2 + self.BUTTON_MARGIN
        left_x = (SCREEN_WIDTH - buttons_width) // 2
        right_x = left_x + self.BUTTON_WIDTH + self.BUTTON_MARGIN
        y = int(SCREEN_HEIGHT * 0.55)
        button.standard_button(left_x, y, self.BUTTON_WIDTH, self.BUTTON_HEIGHT, 2, GRAY, WHITE, "Play again", get_font_default(), play_again)
        button.standard_button(right_x, y, self.BUTTON_WIDTH, self.BUTTON_HEIGHT, 2, GRAY, WHITE, "Quit", get_font_default(), quit_to_map)

    def unload(self):
        pass

def play_again():
    navigate_to(singleton.previous_state)

def quit_to_map():
    navigate_to(GameState.MAP)
