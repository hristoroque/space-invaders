import pygame
from .actor import Actor
from lib.vectors import Vector2
from lib.components.image_components import SpriteComponent

class BackGround(Actor):
    def __init__(self, game):
        super().__init__(game)
        self.position = Vector2(self.game.width / 2, 0)
        self.velocity = 100
        sprite = SpriteComponent(self, 0)
        image = self.game.get_image('fondo.png')
        sprite.set_image(pygame.transform.scale(image,(self.game.width, self.game.height*2)))
        self.add_component(sprite)

    def update_actor(self, delta_time):
        self.position.y += delta_time * self.velocity
        if self.position.y > self.game.height:
            self.position.y = 0