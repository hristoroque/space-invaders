import pygame
from .actor import Actor
from lib.vectors import Vector2
from lib.components.image_components import SpriteComponent

class Fire(Actor):
    def __init__(self, game):
        super().__init__(game)
        self.dir = 0
        self.position = Vector2(0,0)
        self.velocity = 300
        self.sprite = SpriteComponent(self, 1)
        image = self.game.get_image('fire.png')
        self.sprite.set_image(pygame.transform.scale(image, (32, 32)))
        self.add_component(self.sprite)

    def update_actor(self, delta_time):
        self.position = self.position.add(
                self.get_forward().times(self.velocity * delta_time)
            )

        if self.position.y < -self.sprite.height:
            self.destroy()