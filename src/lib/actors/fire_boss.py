import pygame
from .actor import Actor
from lib.vectors import Vector2
from lib.components.image_components import SpriteComponent
from lib.components.colliders import CircleCollider

class FireBoss(Actor):
    def __init__(self, game):
        super().__init__(game)
        self.tag = 'enemy_fire'
        self.dir = 0
        self.position = Vector2(0,0)
        self.velocity = 300
        self.velocity_x = 0;
        sprite = SpriteComponent(self, 1)
        image = self.game.get_image('bubble.png')
        sprite.set_image(pygame.transform.scale(image, (100, 100)))
        self.add_component(sprite)

        self.collider = CircleCollider(self)
        self.collider.radius = 40
        self.add_component(self.collider)

    def update_actor(self, delta_time):
        self.position.y += delta_time * 150
        self.position.x += delta_time * self.velocity_x

    
    def set_velocity_x(self, velocity_x):
        self.velocity_x = velocity_x