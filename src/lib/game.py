import pygame
from os import path
from lib.actors.actor import Actor
from lib.actors.ship import Ship
from lib.actors.enemy import Enemy
from lib.actors.bg import BackGround
from lib.components.base import Component
from lib.components.image_components import SpriteComponent

assets = 'assets'

class Game:
    def __init__(self):
        self.actors = []
        self.pending_actors = []
        self.updating_actors = False
        self.sprites = []
        self.horizontalAxis = 0
        self.width = 500
        self.height = 500
        self.fire_button = False
        self.images = {}

    '''Executes the game loop'''
    def initialize(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.ticksCount = 0
        self.is_running = True
        self.load_data()

    def load_data(self):
        ship = Ship(self)
        bg = BackGround(self)
        enemy = Enemy(self)
        self.add_actor(enemy)
        self.add_actor(ship)
        self.add_actor(bg)

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
                if event.key == pygame.K_SPACE:
                    self.fire_button = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.horizontalAxis = 0
                if event.key == pygame.K_SPACE:
                    self.fire_button = False
        for actor in self.actors:
            actor.process_input({
                'horizontal_axis': self.horizontalAxis,
                'fire_button': self.fire_button,
            })
    
    def update(self):
        delta_time = (pygame.time.get_ticks() - self.ticksCount) / 1000
        self.ticksCount = pygame.time.get_ticks()

        self.updating_actors = True
        for actor in self.actors:
            actor.update(delta_time)
        self.updating_actors = False
        
        for actor in self.pending_actors:
            self.actors.append(actor)

        self.actors = [actor for actor in self.actors if actor.state != Actor.State.DEATH]
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

    def get_image(self, filename):
        if filename in self.images:
            return self.images[filename]
        else:
            image = pygame.image.load(path.join(assets,filename))
            self.images[filename] = image
            return self.images[filename]

    def add_sprite(self, sprite_component):
        draw_order = sprite_component.draw_order

        index = 0
        for sprite in self.sprites:
            if draw_order < sprite.draw_order:
                break
            index+=1

        self.sprites.insert(index, sprite_component)

    def remove_sprite(self, sprite_component):
        self.sprites = [sprite for sprite in self.sprites if sprite != sprite_component]