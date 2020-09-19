import pygame
from os import path

assets = 'assets'

image = pygame.image.load(path.join(assets,'player.png'))
print(image.get_rect().size)