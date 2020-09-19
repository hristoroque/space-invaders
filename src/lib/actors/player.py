from .actor import Actor
from lib.vectors import Vector2

class Player(Actor):
    def __init__(self, game):
        super().__init__(game)
        self.position.y = -500
        self.velocity = 100

    def update(self, delta_time):
        self.position.y += delta_time * self.velocity
        if self.position.y >= 0:
            self.position.y = -500