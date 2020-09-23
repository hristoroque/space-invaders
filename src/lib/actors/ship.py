import pygame
from pygame import mixer

from lib.vectors import Vector2
from lib.components.image_components import SpriteComponent
from lib.components.move_components import InputComponent, SpaceInvaderMovement
from lib.components.colliders import CircleCollider
from .actor import Actor
from .powerups import MultipleShootStrategy, SimpleShootStrategy


class Ship(Actor):
    def __init__(self, game):
        super().__init__(game)
        self.dir = 0
        self.firing = False
        self.can_fire = True
        self.reload_time = 0.2
        self.curr_time = 0
        self.power_up_time = 5
        self.shooting_strategy = SimpleShootStrategy()
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
        if input_state[pygame.K_SPACE] and not self.firing:
            self.firing = True
            self.shooting_strategy.shoot(self)
            self.game.get_sound('laser.wav').play()

    def update_actor(self, delta_time):
        # print(self.curr_time)
        if self.firing:
            self.curr_time += delta_time
        if self.curr_time >= self.reload_time:
            self.firing = False
            self.curr_time = 0

    def shoot(self):
        self.shooting_strategy.shoot(self)

    def on_collide(self, actor):
        if actor.tag == 'powerup':
            actor.destroy()
            self.shooting_strategy = MultipleShootStrategy()


class EnemyShip(Actor):
    def __init__(self, game):
        super().__init__(game)
        self.tag = 'enemy'
        self.position = Vector2(self.game.width/2, self.game.height/2)
        self.movement_component = SpaceInvaderMovement(self)
        self.sprite = SpriteComponent(self, 4)
        image = self.game.get_image('ufo.png')
        self.sprite.set_image(image)
        self.collider = CircleCollider(self)
        self.collider.radius = 12

        self.add_component(self.collider)
        self.add_component(self.sprite)
        self.add_component(self.movement_component)

    def process_input_actor(self, input_state):
        pass

    def update_actor(self, delta_time):
        pass
