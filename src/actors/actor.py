import pygame
from pygame import Rect

class Actor:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def update(self, deltaTime, horizontalAxis):
        self.x += deltaTime * horizontalAxis * 100

    def render(self, screen):
        pygame.draw.rect(screen, (255,255,120), Rect(
            self.x,
            self.y,
            10,
            10,
        ))
        pygame.display.update()
    