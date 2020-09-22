import pygame
import math
from .actor import Actor
from lib.components.image_components import SpriteComponent
from lib.components.move_components import MoveComponent
from lib.actors.fire import Fire
from lib.vectors import Vector2
import math


class PowerUp(Actor):
    def __init__(self, game):
        super().__init__(game)

        self.position = Vector2(self.game.width/2, 0)
        self.rotation = math.radians(-90)

        sprite = SpriteComponent(self, 5)
        image = self.game.get_image('powerup.png')
        sprite.set_image(pygame.transform.scale(image, (32, 32)))
        self.add_component(sprite)

        self.component = MoveComponent(self)
        self.component.forward_speed = 100
        self.add_component(self.component)


class ShootingStrategy():
    def shoot(self, actor):
        pass


class SimpleShootStrategy(ShootingStrategy):
    def shoot(self, actor):
        game = actor.game
        fire = Fire(game)
        fire.position = Vector2(actor.position.x, actor.position.y)
        game.add_actor(fire)


class MultipleShootStrategy(ShootingStrategy):
    def shoot(self, actor):
        game = actor.game
        fires = [Fire(game), Fire(game), Fire(game)]
        fires[0].rotation = math.radians(90)
        fires[1].rotation = math.radians(100)
        fires[2].rotation = math.radians(80)

        for fire in fires:
            fire.position = Vector2(actor.position.x, actor.position.y)
            game.add_actor(fire)
