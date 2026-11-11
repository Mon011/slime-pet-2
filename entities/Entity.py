import typing
import uuid
from components import Component

class Entity:
    id: int
    components: list[Component]

    def __init__(self, *components: Component):
        self.id = uuid.uuid1() 
        self.components = list(components)

    def get_component(self, component_type: type) -> Component:
        for c in self.components:
            if component_type == type(c):
                return c

    def has_component(self, component_type: type):
        if issubclass(component_type, Component):
            return True
    