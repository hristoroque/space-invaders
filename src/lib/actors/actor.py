import pygame
import math
from pygame import Rect
from lib.vectors import Vector2
from enum import Enum

class Actor:
    class State(Enum):
        ACTIVE = 0
        PAUSE = 1
        DEATH = 2

    def __init__(self, game):
        self.position = Vector2(0, 0)
        self.scale = 1
        self.rotation = 0
        self.components = []
        self.game = game
        self.state = Actor.State.ACTIVE

    def start(self):
        pass

    def process_input(self, keyboard):
        pass

    def update(self, delta_time):
        self.update_components(delta_time)
        self.update_actor(delta_time)

    def update_components(self, delta_time):
        for component in self.components:
            component.update(delta_time)

    def update_actor(self, delta_time):
        pass

    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, component):
        pass

    def get_forward(self):
        return Vector2(
            math.cos(self.rotation),
            -math.sin(self.rotation)
            )
