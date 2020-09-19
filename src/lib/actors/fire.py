from .actor import Actor
from lib.vectors import Vector2
from lib.components.image_components import SpriteComponent

class Fire(Actor):
    def __init__(self, game):
        super().__init__(game)
        self.dir = 0
        self.position = Vector2(0,0)
        self.velocity = 300
        sprite = SpriteComponent(self, 1)
        sprite.set_image(self.game.get_image('fire.png'))
        self.add_component(sprite)

    def update_actor(self, delta_time):
        self.position.y -= delta_time * 100