from .actor import Actor
import math
from lib.components.image_components import SpriteComponent
from lib.components.move_components import MoveComponent
from lib.vectors import Vector2

class Enemy(Actor):
    def __init__(self, game):
        super().__init__(game)
        
        self.position = Vector2(game.width/2, game.height/2)
        self.rotation = math.pi/2
        self.speed = 12.0
        image = self.game.get_image('ufo.png')
        sprite = SpriteComponent(self, 1)
        sprite.set_image(image)
        self.add_component(sprite)
        move_component = MoveComponent(self)
        move_component.forward_speed = 20
        move_component.angular_speed = 0
        self.add_component(move_component)
