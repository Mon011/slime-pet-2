from systems import * 
from pyray import *
from config import *
from components import *
import string_resources as res

class Engine:
    entities: list
    systems: list

    def run(self):
        init_window(SCREEN_WIDTH, SCREEN_HEIGHT, res.TITLE)
        set_target_fps(TARGET_FPS)
        ui_system = UISystem()
        systems = [SurvivalSystem(), EntityGeneratorSystem(), ControlSystem(), MovementSystem(), CollisionSystem(), RenderSystem()]

        ui_system.load()

        for system in systems:
            system.load()

        while not window_should_close():
            begin_drawing()
            previous_state = singleton.state
            
            if previous_state != singleton.state:
                ui_system.unload()
            
            ui_system.update()
            
            for system in systems:
                system.update()

            if previous_state != singleton.state:
                ui_system.load()
                
            end_drawing()

        for system in systems:
            system.unload()
        close_window()

engine = Engine()
