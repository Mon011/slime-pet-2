from .system import System
from components import *
from scenes import *
from entities import slime, Entity
import time

class SurvivalSystem(System):
    last_sync_time: float = time.time()
    hunger_increase: int = 0 

    def load(self):
        pass 

    def update(self):
        if(slime.hunger > 0):
            if(singleton.state == GameState.PARK or
               singleton.state == GameState.TOWN):
                self.last_sync_time = time.time()
                if(slime.hunger <= self.hunger_increase):
                    slime.hunger = 0
                elif(self.hunger_increase > 0):
                    slime.hunger -= self.hunger_increase
                    self.hunger_increase = 0

            if(singleton.state == GameState.SHOP or 
                singleton.state == GameState.PLAYGROUND):
                self.hunger_increase = int((time.time() - self.last_sync_time) // 1); 
                        
        if(slime.hunger == 0):
           if(time.time() > self.last_sync_time):
               slime.healthpoints -= 1
               self.last_sync_time = time.time()
           if(slime.healthpoints == 0): 
               slime.healthpoints = 0 

    def unload(self):
        pass
    