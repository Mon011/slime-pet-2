from .system import System
from components import *
from entities import EntityType, Entity
from events import OnGameOverEvent, on_event
from pyray import *

class CollisionSystem(System):

    def load(self):
        pass

    def update(self):
        slime = self._get_slime_entity()
        if(slime is None):
            return

        self._check_collision(slime)

    def unload(self):
        pass

    def _get_slime_entity(self) -> Entity:
        for entity in singleton.state_data.entities:
            if entity.type == EntityType.SLIME:
                return entity

    def _check_collision(self, slime: Entity):
        slime_hitbox = self._get_hitbox_rectangle(slime)
        if slime_hitbox is None:
            return

        for entity in list(singleton.state_data.entities):
            if entity is slime:
                continue

            hitbox = self._get_hitbox_rectangle(entity)
            if hitbox is None or not check_collision_recs(slime_hitbox, hitbox):
                continue

            collectible = entity.get_component(Collectible)
            if collectible is not None:
                collectible.on_collect()
                singleton.state_data.entities.remove(entity)
                continue

            obstacle = entity.get_component(Obstacle)
            if obstacle is not None and obstacle.is_deadly:
                on_event(OnGameOverEvent())
                return

    def _get_hitbox_rectangle(self, entity: Entity) -> Rectangle:
        hitbox = entity.get_component(Hitbox)
        position = entity.get_component(Position)
        if hitbox is None or position is None:
            return None

        return Rectangle(
            position.x + hitbox.rectangle.x,
            position.y + hitbox.rectangle.y,
            hitbox.rectangle.width,
            hitbox.rectangle.height,
        )
