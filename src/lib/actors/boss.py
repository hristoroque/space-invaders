import pygame
from .actor import Actor
import math
from lib.components.image_components import SpriteComponent
from lib.components.image_components import LifeRectComponent
from lib.components.move_components import MoveComponent
from lib.components.colliders import CircleCollider
from lib.vectors import Vector2
from .fire_boss import FireBoss


class Boss(Actor):
    def __init__(self, game):
        super().__init__(game)
        self.lifes = 100
        self.timer_shoot = 0
        self.position = Vector2(game.width/2, 100)
        self.rotation = math.pi/2
        self.speed = 6.0
        self.screen = game.screen
        image = self.game.get_image('boss01.png')

        self.spriteLife = LifeRectComponent(self, self.lifes, 1)
        self.spriteLife.set_offset(75, 60)
        self.spriteLife.lifes = self.lifes
        self.add_component(self.spriteLife)

        sprite = SpriteComponent(self, 1)
        sprite.set_image(image)
        self.add_component(sprite)

        self.move_component = MoveComponent(self)
        self.move_component.forward_speed = 0
        self.move_component.angular_speed = 0
        self.move_component.side_speed = -0.4
        self.add_component(self.move_component)

        self.collider = CircleCollider(self)
        self.collider.radius = 70
        self.add_component(self.collider)

    def update(self, delta_time):
        super(Boss, self).update(delta_time)
        if(self.timer_shoot == 0):
            self.timer_shoot = 300
            self.shoot()
        self.timer_shoot = self.timer_shoot - 1

        if (self.position.x < 80):
            self.move_component.side_speed = 0.7
        elif (self.position.x > 420):
            self.move_component.side_speed = -0.7

    def shoot(self):
        fire = FireBoss(self.game)
        fire.set_velocity_x((self.game.ship.position.x - self.position.x) / 3)
        fire.position = Vector2(self.position.x, self.position.y)
        self.game.add_actor(fire)

    def on_collide(self, actor):
        if actor.tag == 'player_fire':
            actor.destroy()
            self.lifes -= 1
            self.spriteLife.lifes = self.lifes
            if(self.lifes == 0):
                self.destroy()
