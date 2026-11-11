from pyray import *
from .component import Component
import typing

class Clickable(Component):
    on_click: callable

    def __init__(self, on_click):
       self.on_click = on_click 
       