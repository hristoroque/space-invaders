import pygame

from lib.vectors import Vector2
from lib.components.image_components import SpriteComponent
from lib.components.move_components import InputComponent, SpaceInvaderMovement
from lib.components.colliders import CircleCollider
from .actor import Actor
from .powerups import MultipleShootStrategy


class Ship(Actor):
    def __init__(self, game):
        super().__init__(game)
        self.dir = 0
        self.firing = False
        self.can_fire = True
        self.reload_time = 10
        self.curr_time = 0
        self.shooting_strategy = MultipleShootStrategy()
        self.position = Vector2(self.game.width / 2, self.game.height - 42)
        self.velocity = 250
        sprite = SpriteComponent(self, 3)
        image = self.game.get_image('player.png')
        sprite.set_image(pygame.transform.scale(image, (64, 64)))
        self.add_component(sprite)
        self.input_component: InputComponent = InputComponent(self)
        self.add_component(self.input_component)
        self.collider = CircleCollider(self)
        self.collider.radius = 32
        self.add_component(self.collider)

    def process_input_actor(self, input_state):
        pass

    def update_actor(self, delta_time):
        pass

    def shoot(self):
        self.shooting_strategy.shoot(self)

    def on_collide(self, actor):
        print(f'colliding with {actor}')


class EnemyShip(Actor):
    def __init__(self, game):
        super().__init__(game)
        self.position = Vector2(self.game.width/2, self.game.height/2)
        self.movement_component = SpaceInvaderMovement(self)
        self.sprite = SpriteComponent(self, 4)
        image = self.game.get_image('ufo.png')
        self.sprite.set_image(image)

        self.add_component(self.sprite)
        self.add_component(self.movement_component)

    def process_input_actor(self, input_state):
        pass

    def update_actor(self, delta_time):
        pass
