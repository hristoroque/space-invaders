import pygame
from lib.vectors import Vector2
from .actor import Actor

class Ship(Actor):
    def __init__(self, game):
        super().__init__(game)
        self.dir = 0
        self.position = Vector2(self.game.width/2, self.game.height - 50)
        self.velocity = 250

    def process_input(self, horizontal_axis):
        self.dir = horizontal_axis

    def update_actor(self, delta_time):
        self.position.x += self.dir * delta_time * self.velocity