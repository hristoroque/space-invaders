import pygame
from lib.vectors import Vector2
from lib.components.image_components import SpriteComponent
from .actor import Actor
from .fire import Fire

class Ship(Actor):
    def __init__(self, game):
        super().__init__(game)
        self.dir = 0
        self.firing = False
        self.can_fire = True
        self.reload_time = 100
        self.curr_time = 0
        self.position = Vector2(self.game.width / 2, self.game.height/ 2)
        self.velocity = 250
        sprite = SpriteComponent(self, 1)
        image = self.game.get_image('ship.png')
        sprite.set_image(pygame.transform.scale(image,(32, 32)))
        self.add_component(sprite)

    def process_input(self, keyboard):
        self.dir = keyboard['horizontal_axis']
        self.firing = keyboard['fire_button']

    def update_actor(self, delta_time):
        self.position.x += self.dir * delta_time * self.velocity
        if self.firing and self.can_fire:
            self.shoot()
            self.can_fire = False
            self.curr_time = 0
        
        if not self.can_fire:
            self.curr_time += 1

        if self.curr_time > self.reload_time:
            self.can_fire = True

    def shoot(self):
        fire = Fire(self.game)
        fire.position = Vector2(self.position.x, self.position.y)
        self.game.add_actor(fire)