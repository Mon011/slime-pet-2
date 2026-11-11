from .Component import Component
from pyray import *

class Render(Component):
    texture: Texture
    source_rectangle: Rectangle
    is_animated: bool
    rotation: int

    def __init__(self, texture, source_rectangle, is_animated, rotation):
        self.texture = texture
        self.source_rectangle = source_rectangle
        self.is_animated = is_animated
        self.rotation = rotation

# Component.register(Render)