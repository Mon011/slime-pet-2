from .System import System
from components import *
from pyray import *
from entities import Entity

class RenderSystem(System):

    def load(self):
        pass
    
    def update(self):
        pass
        # for entity in singleton.state_data.entities:
            # if(entity.has_component(Render)):
                # render = entity.get_component(Render)

    def unload(self):
        pass
