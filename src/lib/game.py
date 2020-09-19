import pygame
from os import path
from lib.actors.actor import Actor
from lib.components.base import Component
from lib.components.image_components import SpriteComponent

assets = 'assets/'

class Game:
    def __init__(self):
        self.actors = []
        self.pending_actors = []
        self.updating_actors = False
        self.sprites = []

    '''Executes the game loop'''
    def initialize(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500,500))
        self.ticksCount = 0
        self.is_running = True
        self.load_data()

    def load_data(self):
        bg = Actor(self)
        sprite = SpriteComponent(bg, 1)
        #pygame.image.load()
        sprite.set_image(pygame.image.load(path.join(assets,'player.png')))
        self.add_actor(bg)
        self.add_sprite(sprite)

    def shutdown(self):
        print("Shutting down game. Good Bye!")
        self.is_running = False

    def run(self):
        while(self.is_running):
            self.process_input()
            self.update()
            self.render()

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.shutdown()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.shutdown()
                if event.key == pygame.K_LEFT:
                    self.horizontalAxis = -1
                if event.key == pygame.K_RIGHT:
                    self.horizontalAxis = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.horizontalAxis = 0
    
    def update(self):
        delta_time = (pygame.time.get_ticks() - self.ticksCount) / 1000
        self.ticksCount = pygame.time.get_ticks()

        self.updating_actors = True
        for actor in self.actors:
            actor.update(delta_time)
        self.updating_actors = False
        
        for actor in self.pending_actors:
            self.actors.append(actor)

        self.pending_actors.clear()

    def render(self):
        self.screen.fill((50, 0, 0))
        for sprite in self.sprites:
            sprite.draw(self.screen)
        pygame.display.update()
    
    def add_actor(self, actor):
        if self.updating_actors:
            self.pending_actors.append(actor)
        else:
            self.actors.append(actor)

    def remove_actor(self, actor):
        pass

    def add_sprite(self, sprite_component):
        draw_order = sprite_component.draw_order

        index = 0
        for sprite in self.sprites:
            if draw_order < sprite.draw_order:
                break
            index+=1

        self.sprites.insert(index, sprite_component)