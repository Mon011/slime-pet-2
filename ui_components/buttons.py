from pyray import *

def calculate_font_size(font: Font, text: str, rectangle: Rectangle, spacing: float, text_scale: int = 2):
    font_size = rectangle.height
    text_size = measure_text_ex(font, text, font_size, spacing)

    scale_x = rectangle.width / text_size.x / text_scale 
    scale_y = rectangle.height / text_size.y / text_scale
    font_size *= min(scale_x, scale_y)
    return font_size

def standard_button(x :float, y: float, width: float, height: float, line_thick: int, rect_fill_color: Color, rect_border_color: Color, text: str, font: Font, on_click: callable, text_spacing: float = 0.0):
    rectangle = Rectangle(x, y, width, height)
    draw_rectangle_rec(rectangle, rect_fill_color)
    draw_rectangle_lines_ex(rectangle, line_thick, rect_border_color)
    font_size = calculate_font_size(font, text, rectangle, text_spacing)
    text_size = measure_text_ex(font, text, font_size, text_spacing)

    text_pos_x = int(rectangle.x + (rectangle.width - text_size.x) / 2 - line_thick)
    text_pos_y = int(rectangle.y + (rectangle.height - text_size.y ) / 2)
    draw_text(text, text_pos_x, text_pos_y, int(font_size), BLACK)

    mouse_pos = get_mouse_position()
    if check_collision_point_rec(mouse_pos, rectangle) and is_mouse_button_released(0):
        on_click()

def standard_texture_button(texture: Texture, x: int, y: int):
    draw_texture(texture, x, y, WHITE)

def multiple_state_button(texture: Texture2D, x: int, y: int, scale: int, on_click):
    frame_height = texture.height / 3
    
    scaled_height = frame_height * scale
    scaled_width = texture.width * scale

    button_bounds = Rectangle(x, y, scaled_width, scaled_height)
    source_rec = Rectangle(x, y, texture.width, frame_height)

    mouse_point = get_mouse_position()
    state = 0

    if check_collision_point_rec(mouse_point, button_bounds):
        if is_mouse_button_released(0):
            on_click() 
        if is_mouse_button_down(0):
            state = 2
        else:
            state = 1
    
    source_rec.y = state * frame_height
    draw_texture_pro(texture, source_rec, Rectangle(x, y, scaled_width, scaled_height), [0, 0], 0, WHITE)
