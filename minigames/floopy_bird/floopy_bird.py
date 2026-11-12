import random
from components import singleton, Position, Movement, Hitbox
from components.direction import Direction
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from entities import Entity, EntityType, create_slime, create_border_up, create_border_down, create_coin, SLIME_HEIGHT, COIN_WIDTH, COIN_HEIGHT
from events import on_event, OnCoinIncreaseEvent
from minigames.minigame import Minigame
from .entities import create_tubes, TUBE_WIDTH, TUBE_SPEED

class FloopyBird(Minigame):
    MAX_TUBES = 50
    TUBE_GAP = 200
    TUBE_SPACING = 300
    TUBE_MIN_HEIGHT = 60
    COIN_GRANT_VALUE = 1

    def start(self):
        self.add_entity(create_slime(SCREEN_WIDTH * 0.2, (SCREEN_HEIGHT - SLIME_HEIGHT) / 2))
        self.add_entity(create_border_up(is_deadly=True))
        self.add_entity(create_border_down(is_deadly=True))

    def update(self):
        self._remove_passed_entities()
        self._generate_tubes()

    def _remove_passed_entities(self):
        entities = singleton.state_data.entities
        entities[:] = [e for e in entities if not self._is_passed(e)]

    def _is_passed(self, entity: Entity) -> bool:
        position = entity.get_component(Position)
        hitbox = entity.get_component(Hitbox)
        return position.x + hitbox.rectangle.width < 0

    def _generate_tubes(self):
        tubes = self._get_tubes()
        last_x = max((t.get_component(Position).x for t in tubes), default=SCREEN_WIDTH - self.TUBE_SPACING)

        while len(tubes) + 1 <= self.MAX_TUBES:
            last_x += self.TUBE_SPACING
            gap_y = random.randint(self.TUBE_MIN_HEIGHT, SCREEN_HEIGHT - self.TUBE_MIN_HEIGHT - self.TUBE_GAP)
            for tube in create_tubes(last_x, gap_y, self.TUBE_GAP):
                self.add_entity(tube)
                tubes.append(tube)
            self.add_entity(self._generate_coin(last_x, gap_y))

    def _generate_coin(self, tube_x: float, gap_y: float) -> Entity:
        x = tube_x + (TUBE_WIDTH - COIN_WIDTH) / 2
        y = gap_y + (self.TUBE_GAP - COIN_HEIGHT) / 2
        return create_coin(x, y, self._collect_coin, Movement(TUBE_SPEED, Direction.LEFT))

    def _collect_coin(self):
        on_event(OnCoinIncreaseEvent(self.COIN_GRANT_VALUE))

    def _get_tubes(self) -> list[Entity]:
        return [e for e in singleton.state_data.entities if e.type == EntityType.TUBE]
