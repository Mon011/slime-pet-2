from .component import Component
from pyray import *

class Render(Component):
    texture_path: str             
    source_rectangle: Rectangle   
    is_animated: bool
    rotation: int

    def __init__(self, texture_path, source_rectangle = None, is_animated = False, rotation = 0):
        self.texture_path = texture_path
        self.source_rectangle = source_rectangle
        self.is_animated = is_animated
        self.rotation = rotation

