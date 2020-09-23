from enum import Enum
from typing import List
import pygame
import math
from pygame import Rect
from lib.vectors import Vector2
from lib.components.base import Component


class Actor:
    class State(Enum):
        ACTIVE = 0
        PAUSE = 1
        DEATH = 2

    def __init__(self, game):
        self.tag = 'gameobject'
        self.position = Vector2(0, 0)
        self.scale = 1
        self.rotation = 0
        self.components: List[Component] = []
        self.game = game
        self.state = Actor.State.ACTIVE
        self.start()

    def start(self):
        pass

    def process_input(self, input_state):
        for component in self.components:
            component.process_input(input_state)
        self.process_input_actor(input_state)

    def process_input_actor(self, input_state):
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

    def destroy(self):
        self.state = Actor.State.DEATH
        for component in self.components:
            component.destroy()

    def on_collide(self, actor):
        pass
