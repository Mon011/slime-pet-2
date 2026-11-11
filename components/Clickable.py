from pyray import *
from .Component import Component
import typing

class Clickable(Component):
    on_click: callable

    def __init__(self, on_click):
       self.on_click = on_click 

# Component.register(Clickable)