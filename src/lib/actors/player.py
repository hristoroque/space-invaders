from .actor import Actor
from lib.vectors import Vector2

class Player(Actor):
    def __init__(self, game):
        super().__init__(game)
        self.position.y = -500

    def update(self, game):
        self.position = self.position.add(Vector2(0,1))
        if self.position.y >= 0:
            self.position.y = -500