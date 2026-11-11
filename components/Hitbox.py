from .Component import Component
from pyray import *

class Hitbox(Component):
    rectangle: Rectangle 

    def __init__(self, rectangle):
        self.rectangle = rectangle
        
# Component.register(Hitbox)