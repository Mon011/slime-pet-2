import random
from components import singleton, Position
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from entities import Entity, EntityType, create_slime, SLIME_HEIGHT
from minigames.minigame import Minigame
from .entities import create_tubes

class FloopyBird(Minigame):
    MAX_TUBES = 50
    TUBE_GAP = 200
    TUBE_SPACING = 300
    TUBE_MIN_HEIGHT = 60

    def start(self):
        self.add_entity(create_slime(SCREEN_WIDTH * 0.2, (SCREEN_HEIGHT - SLIME_HEIGHT) / 2))

    def update(self):
        self._generate_tubes()

    def _generate_tubes(self):
        tubes = self._get_tubes()
        last_x = max((t.get_component(Position).x for t in tubes), default=SCREEN_WIDTH - self.TUBE_SPACING)

        while len(tubes) + 1 <= self.MAX_TUBES:
            last_x += self.TUBE_SPACING
            gap_y = random.randint(self.TUBE_MIN_HEIGHT, SCREEN_HEIGHT - self.TUBE_MIN_HEIGHT - self.TUBE_GAP)
            for tube in create_tubes(last_x, gap_y, self.TUBE_GAP):
                self.add_entity(tube)
                tubes.append(tube)

    def _get_tubes(self) -> list[Entity]:
        return [e for e in singleton.state_data.entities if e.type == EntityType.TUBE]
