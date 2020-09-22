from .base import Component
from lib.vectors import Vector2


class CircleCollider(Component):
    def __init__(self, actor):
        super().__init__(actor)
        self.radius = 0

    def get_center(self) -> Vector2:
        return self.actor.position


def intersect(circle_a: CircleCollider, circle_b: CircleCollider):
    diff: Vector2 = circle_a.get_center() - circle_b.get_center()
    distance = diff.length_squared()

    radiiSqr = circle_a.radius + circle_a.radius
    radiiSqr *= 2

    return distance <= radiiSqr
