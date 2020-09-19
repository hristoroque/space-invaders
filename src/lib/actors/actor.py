import pygame
from pygame import Rect
from lib.vectors import Vector2
from enum import Enum

class Actor:
    class State(Enum):
        ACTIVE = 0
        DEATH = 1

    def __init__(self, game):
        self.position = Vector2(0, 0)
        self.scale = 1
        self.rotation = 0
        self.components = []
        self.game = game

    def update(self, delta_time):
        pass

    def update_components(self, delta_time):
        pass

    def update_actor(self, delta_time):
        pass

    def add_component(self, component):
        pass

    def remove_component(self, component):
        pass

    def render(self, screen):
        pass