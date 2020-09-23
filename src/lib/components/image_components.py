import pygame
from .base import Component

class SpriteComponent(Component):
    def __init__(self, actor, draw_order = 1):
        super().__init__(actor)
        self.draw_order = draw_order
        self.image = None
        self.height = 0
        self.width = 0
        self.actor.game.add_sprite(self)

    def process_input(self, input_state):
        pass

    def update(self, delta_time):
        pass

    def set_image(self, image):
        self.image = image
        self.width, self.height = image.get_rect().size

    def draw(self, screen):
        screen.blit(self.image, (
            self.actor.position.x - self.width/2,
            self.actor.position.y - self.height/2
        ))

    def destroy(self):
        self.actor.game.remove_sprite(self)

class LifeRectComponent(Component):
    def __init__(self, actor, max_life, draw_order = 1):
        super().__init__(actor)
        self.draw_order = draw_order
        self.max_life = max_life
        self.step_life = 150 / max_life
        self.image = None
        self.height = 0
        self.width = 0
        self.actor.game.add_sprite(self)
        self.offset_x = 0
        self.offset_y = 0
        self.lifes = 10
    
    def process_input(self, input_state):
        pass

    def update(self, delta_time):
        pass

    def set_offset(self, x, y):
        self.offset_x = x
        self.offset_y = y
    
    def set_image(self, image):
        self.image = image
        self.width, self.height = image.get_rect().size

    def draw(self, screen):
        pygame.draw.rect(screen,(255,0,0),(self.actor.position.x - self.offset_x, self.actor.position.y - self.offset_y - 30, self.step_life * self.max_life, 10))
        pygame.draw.rect(screen,(0,255,0),(self.actor.position.x - self.offset_x, self.actor.position.y - self.offset_y - 30, self.step_life * self.lifes, 10))

    def destroy(self):
        self.actor.game.remove_sprite(self)

