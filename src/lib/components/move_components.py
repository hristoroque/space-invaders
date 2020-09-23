import pygame
from .base import Component
from lib.vectors import Vector2


class MoveComponent(Component):
    def __init__(self, actor, update_order=0):
        super().__init__(actor, update_order)

        self.forward_speed = 0
        self.side_speed = 0
        self.angular_speed = 0

    def process_input(self, input_state):
        pass

    def update(self, delta_time):
        if self.angular_speed != 0:
            new_rotation = self.actor.rotation + self.angular_speed * delta_time
            self.actor.rotation = new_rotation
        if self.forward_speed != 0:
            self.actor.position = self.actor.position.add(
                self.actor.get_forward().times(self.forward_speed * delta_time)
            )
        if self.side_speed != 0:
            self.actor.position = self.actor.position.add(
                Vector2(self.side_speed * delta_time * 50, 0)
            )

    def destroy(self):
        pass


class SpaceInvaderMovement(MoveComponent):
    def __init__(self, actor, update_order=0):
        super().__init__(actor, update_order)
        self.velocity = 80
        self.dir = 1

    def process_input(self, input_state):
        pass

    def update(self, delta_time):
        y = 0
        if self.actor.position.x >= 500:
            self.dir = -1
            y = 50
        elif self.actor.position.x <= 0:
            self.dir = 1
            y = 50

        self.actor.position.y += y
        self.actor.position.x += delta_time * self.velocity * self.dir


class InputComponent(MoveComponent):
    def __init__(self, actor, update_order=0):
        super().__init__(actor, update_order)
        self.velocity = 300
        self.dir = 0

    def process_input(self, input_state):
        self.dir = 0
        if input_state[pygame.K_LEFT]:
            self.dir -= 1
        if input_state[pygame.K_RIGHT]:
            self.dir += 1

    def update(self, delta_time):
        self.actor.position.x += self.dir * delta_time * self.velocity
