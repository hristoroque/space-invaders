import pygame
from .base import Component
from lib.vectors import Vector2


class CircleCollider(Component):
    def __init__(self, actor):
        super().__init__(actor)
        self.radius = 0
        self.actor.game.add_collider(self)

    def process_input(self, input_state):
        pass

    def get_center(self) -> Vector2:
        return self.actor.position

    def update(self, delta_time):
        for collider in self.actor.game.colliders:
            if collider != self and intersect(self, collider):
                self.actor.on_collide(collider.actor)

    def destroy(self):
        self.actor.game.remove_collider(self)


def intersect(circle_a: CircleCollider, circle_b: CircleCollider):
    diff: Vector2 = circle_a.get_center() - circle_b.get_center()
    distance = diff.length_squared()

    radiiSqr = circle_a.radius + circle_b.radius
    radiiSqr *= radiiSqr

    return distance <= radiiSqr
