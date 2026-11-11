from .System import System
from components import *
from scenes import *
from entities import Entity

class UISystem(System):
    _scene: Scene
    
    def load(self):
        if(singleton.state == GameState.MENU):
            self._scene = MenuScene()
        if(singleton.state == GameState.CREDITS):
            self._scene = CreditsScene()
        if(singleton.state == GameState.INTRODUCTION):
            self._scene = IntroductionScene()
        if(singleton.state == GameState.PARK):
            self._scene = ParkScene()
        if(singleton.state == GameState.TOWN):
            self._scene = TownScene()
        if(singleton.state == GameState.MAP):
            self._scene = MapScene()
        if(singleton.state == GameState.SHOP):
            self._scene = ShopScene()
        if(singleton.state == GameState.PLAYGROUND):
            self._scene = PlaygroundScene()
        if(singleton.state == GameState.FLOOPY_BIRD):
            self._scene = FloopyBirdScene()
            
        self._scene.load()

    def update(self):
        self._scene.render()

    def unload(self):
        self._scene.unload()
