import typing
from pyray import Rectangle
from components import Component, Render, Position, Hitbox, Movement, Controllable
from components.direction import Direction
from config import DEFAULT_TEXTURE_SCALE
import texture_resources as tex
from .entity_type import EntityType

class Entity:
    type: EntityType
    components: list[Component]

    def __init__(self, entity_type: EntityType, *components: Component):
        self.type = entity_type
        self.components = list(components)

    def get_component(self, component_type: type) -> Component:
        for c in self.components:
            if component_type == type(c):
                return c

    def has_component(self, component_type: type) -> bool:
        return self.get_component(component_type) is not None


SLIME_WIDTH = 34 * DEFAULT_TEXTURE_SCALE
SLIME_HEIGHT = 24 * DEFAULT_TEXTURE_SCALE

def create_slime(x: float, y: float) -> Entity:
    return Entity(
        EntityType.SLIME,
        Render(tex.SLIME_SPRITE),
        Position(x, y),
        Hitbox(Rectangle(0, 0, SLIME_WIDTH, SLIME_HEIGHT)),
        Movement(0, Direction.NONE),
        Controllable(),
    )
