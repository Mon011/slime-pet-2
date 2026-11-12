import typing
from pyray import Rectangle
from components import Component, Render, Position, Hitbox, Movement, Controllable, Gravity, Obstacle, Collectible
from components.direction import Direction
from config import SCREEN_WIDTH, SCREEN_HEIGHT, DEFAULT_TEXTURE_SCALE
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
SLIME_SPEED = 5

def create_slime(x: float, y: float) -> Entity:
    return Entity(
        EntityType.SLIME,
        Render(tex.SLIME_SPRITE),
        Position(x, y),
        Hitbox(Rectangle(0, 0, SLIME_WIDTH, SLIME_HEIGHT)),
        Movement(SLIME_SPEED, Direction.NONE),
        Controllable(up=True, down=True, left=True, right=True, jump=True),
        Gravity()
    )

BORDER_THICKNESS = 10

def create_border_up(is_deadly: bool = False, damage: int = 0) -> Entity:
    return _create_border(EntityType.BORDER_UP, 0, -BORDER_THICKNESS, SCREEN_WIDTH, BORDER_THICKNESS, is_deadly, damage)

def create_border_down(is_deadly: bool = False, damage: int = 0) -> Entity:
    return _create_border(EntityType.BORDER_DOWN, 0, SCREEN_HEIGHT, SCREEN_WIDTH, BORDER_THICKNESS, is_deadly, damage)

def create_border_left(is_deadly: bool = False, damage: int = 0) -> Entity:
    return _create_border(EntityType.BORDER_LEFT, -BORDER_THICKNESS, 0, BORDER_THICKNESS, SCREEN_HEIGHT, is_deadly, damage)

def create_border_right(is_deadly: bool = False, damage: int = 0) -> Entity:
    return _create_border(EntityType.BORDER_RIGHT, SCREEN_WIDTH, 0, BORDER_THICKNESS, SCREEN_HEIGHT, is_deadly, damage)

def _create_border(entity_type: EntityType, x: float, y: float, width: float, height: float, is_deadly: bool, damage: int) -> Entity:
    return Entity(
        entity_type,
        Position(x, y),
        Hitbox(Rectangle(0, 0, width, height)),
        Obstacle(is_deadly, damage),
    )

COIN_WIDTH = 16 * DEFAULT_TEXTURE_SCALE
COIN_HEIGHT = 16 * DEFAULT_TEXTURE_SCALE

def create_coin(x: float, y: float, on_collect: callable, movement: Movement = None) -> Entity:
    components = [
        Render(tex.COIN),
        Position(x, y),
        Hitbox(Rectangle(0, 0, COIN_WIDTH, COIN_HEIGHT)),
        Collectible(on_collect),
    ]
    if movement is not None:
        components.append(movement)
    return Entity(EntityType.COIN, *components)
