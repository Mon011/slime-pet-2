from pyray import Rectangle
from components import Render, Position, Hitbox, Movement, Obstacle
from components.direction import Direction
from config import SCREEN_HEIGHT, DEFAULT_TEXTURE_SCALE
from entities import Entity, EntityType
import texture_resources as tex

TUBE_WIDTH = 40 * DEFAULT_TEXTURE_SCALE
TUBE_SPEED = 5

def create_tubes(x: float, gap_y: float, gap_height: float) -> tuple[Entity, Entity]:
    bottom_y = gap_y + gap_height
    top = _create_tube(x, 0, gap_y, flipped=True)
    bottom = _create_tube(x, bottom_y, SCREEN_HEIGHT - bottom_y, flipped=False)
    return top, bottom

def _create_tube(x: float, y: float, height: float, flipped: bool) -> Entity:
    source_height = height / DEFAULT_TEXTURE_SCALE
    if flipped:
        source_height = -source_height

    return Entity(
        EntityType.TUBE,
        Render(tex.TUBE, Rectangle(0, 0, TUBE_WIDTH / DEFAULT_TEXTURE_SCALE, source_height)),
        Position(x, y),
        Hitbox(Rectangle(0, 0, TUBE_WIDTH, height)),
        Movement(TUBE_SPEED, Direction.LEFT),
        Obstacle(is_deadly=True, damage=0),
    )
