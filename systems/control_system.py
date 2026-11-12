from .system import System
from components import *
from entities import Entity
from pyray import *
from config import SCREEN_HEIGHT, BORDER_DOWN_MARGIN

class ControlSystem(System):

    BORDER_DOWN_MARGIN = 20

    def load(self):
        pass

    def update(self):
        for entity in singleton.state_data.entities:
            controllable = entity.get_component(Controllable)
            if controllable is not None:
                self._move(entity, controllable)
                self._include_gravity_force(entity)

    def unload(self):
        pass

    def _move(self, entity: Entity, controllable: Controllable):
        position = entity.get_component(Position)
        movement = entity.get_component(Movement)
        if position is None or movement is None:
            return

        if controllable.up and is_key_down(KEY_W):
            position.y -= movement.speed
        if controllable.down and is_key_down(KEY_S):
            position.y += movement.speed
        if controllable.left and is_key_down(KEY_A):
            position.x -= movement.speed
        if controllable.right and is_key_down(KEY_D) and not self._exceeds_border_down(position.y):
            position.x += movement.speed
        if controllable.jump and is_key_down(KEY_SPACE):
            position.y -= 10

    def _include_gravity_force(self, entity: Entity):
        if entity.has_component(Gravity):
            g_force = entity.get_component(Gravity).g
            position = entity.get_component(Position)
            if not self._exceeds_border_down(position.y):
                position.y += g_force * 5

        
    def _exceeds_border_down(self, y):
        return y >= SCREEN_HEIGHT - BORDER_DOWN_MARGIN
