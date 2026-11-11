from .system import System
from components import *
from config import DEFAULT_TEXTURE_SCALE
from pyray import *

class RenderSystem(System):
    scale: float
    textures: dict  

    def __init__(self, scale: float = DEFAULT_TEXTURE_SCALE):
        self.scale = scale
        self.textures = {}

    def load(self):
        pass

    def update(self):
        used_textures = set()

        for entity in singleton.state_data.entities:
            render = entity.get_component(Render)
            if render is None:
                continue
            used_textures.add(render.texture_path)

            position = entity.get_component(Position)
            if position is not None:
                self.render_entity(render, position)

        self._unload_unused_textures(used_textures)

    def render_entity(self, render: Render, position: Position):
        texture = self.get_texture(render.texture_path)

        source = render.source_rectangle
        if source is None:
            source = Rectangle(0, 0, texture.width, texture.height)
        width = abs(source.width) * self.scale
        height = abs(source.height) * self.scale

        origin = Vector2(width / 2, height / 2)
        destination = Rectangle(position.x + origin.x, position.y + origin.y, width, height)

        draw_texture_pro(texture, source, destination, origin, render.rotation, WHITE)

    def get_texture(self, path: str) -> Texture:
        if path not in self.textures:
            self.textures[path] = load_texture(path)
        return self.textures[path]

    def _unload_unused_textures(self, used_textures: set):
        for path in [p for p in self.textures if p not in used_textures]:
            unload_texture(self.textures.pop(path))

    def unload(self):
        for texture in self.textures.values():
            unload_texture(texture)
        self.textures.clear()
