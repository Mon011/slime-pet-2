from pyray import *
from config import Scale 
import texture_resources as tex

progress_bar_image = load_image(tex.PROGRESS_BAR)

def calculate_font_size(font: Font, text: str, rectangle: Rectangle, spacing: float, text_scale: int = 2):
    font_size = rectangle.height
    text_size = measure_text_ex(font, text, font_size, spacing)

    scale_x = rectangle.width / text_size.x / text_scale 
    scale_y = rectangle.height / text_size.y / text_scale
    font_size *= min(scale_x, scale_y)
    return font_size

def progress_bar(bar_texture: Texture2D, logo_texture: Texture2D, x: int, y: int, current_progress: int, max_progress: int, color: Color):
    if current_progress > max_progress:
        current_progress = max_progress

    max_width = bar_texture.width * Scale.TRIPLED - (2 * Scale.TRIPLED) 
    render_progress = int(max_width * (current_progress / max_progress))

    draw_rectangle_rec(Rectangle(x + logo_texture.width, y + logo_texture.height // 2, render_progress, bar_texture.height * Scale.TRIPLED), color)
    draw_texture_ex(bar_texture, [x + logo_texture.width, y + logo_texture.height // 2], 0, Scale.TRIPLED, WHITE) 
    draw_texture_ex(logo_texture, [x, y], 0, Scale.TRIPLED, WHITE)

def value_bar(bar_texture: Texture2D, value: str, x: int, y: int, offset: int):
    font_size = calculate_font_size(get_font_default(), value, Rectangle(x, y, bar_texture.width * Scale.TRIPLED - offset, bar_texture.height * Scale.TRIPLED), 0.0)
    draw_texture_ex(bar_texture, [x, y], 0, Scale.TRIPLED, WHITE)
    draw_text(value, x + offset, int(y + (bar_texture.height * 0.75)), int(font_size), WHITE)
