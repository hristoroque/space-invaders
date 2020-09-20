from .base import Component
from lib.vectors import Vector2

class MoveComponent(Component):
    def __init__(self, actor, update_order = 0):
        super().__init__(actor, update_order)

        self.forward_speed = 0
        self.side_speed = 0
        self.angular_speed = 0

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
                Vector2(self.side_speed,0)
            )