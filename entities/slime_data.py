import typing
from .mood import Mood
from pyray import *
# from pathlib import Path
import random

class SlimeData:
    name: str
    healthpoints: int
    hunger: int
    coins: int 
    mood: Mood

    def __init__(self):
        self.healthpoints = 100
        self.hunger = 100
        self.coins = 10
        self.mood = Mood(random.randint(1, 3))
        self.name = "Slimename"

slime = SlimeData()