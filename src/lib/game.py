import pygame
from pygame import mixer

from os import path
from lib.actors.powerups import PowerUp
from lib.actors.actor import Actor
from lib.actors.ship import Ship, EnemyShip, EnemyShips
from lib.actors.enemy import Enemy
from lib.actors.gameover import GameOver
from lib.actors.boss import Boss
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
        self.colliders = []
        self.horizontalAxis = 0
        self.width = 500
        self.height = 500
        self.fire_button = False
        self.images = {}
        self.sounds = {}
        self.is_paused = True
        self.ui_elements = []

    '''Executes the game loop'''

    def initialize(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.ticksCount = 0
        self.is_running = True
        self.load_data()
        self.is_paused = False
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def load_data(self):
        self.ship = Ship(self)
        bg = BackGround(self)
        boss = Boss(self)
        powerup = PowerUp(self)
        enemies = EnemyShips(self)
        game_over = GameOver(self)

        self.add_actor(game_over)
        self.add_actor(powerup)
        self.add_actor(enemies)
        self.add_actor(self.ship)
        self.add_actor(bg)
        self.add_actor(boss)
        mixer.music.load("assets/background.wav")
        mixer.music.set_volume(0.2)
        mixer.music.play(-1)

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

        input_state = pygame.key.get_pressed()

        for actor in self.actors:
            actor.process_input(input_state)

    def update(self):
        pygame.time.delay((self.ticksCount + 16)-pygame.time.get_ticks())

        if not self.is_paused:
            delta_time = (pygame.time.get_ticks() - self.ticksCount) / 1000
            if delta_time > 0.05:
                delta_time = 0.05
        else:
            delta_time = 0

        self.ticksCount = pygame.time.get_ticks()

        self.updating_actors = True
        for actor in self.actors:
            actor.update(delta_time)
        self.updating_actors = False

        for actor in self.pending_actors:
            self.actors.append(actor)

        self.actors = [
            actor for actor in self.actors if actor.state != Actor.State.DEATH]
        self.pending_actors.clear()

    def render(self):
        self.screen.fill((50, 0, 0))
        for sprite in self.sprites:
            sprite.draw(self.screen)
        for ui_element in self.ui_elements:
            ui_element.draw(self.screen)
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
            image = pygame.image.load(path.join(assets, filename))
            self.images[filename] = image
            return self.images[filename]

    def get_sound(self, filename):
        if filename in self.sounds:
            return self.sounds[filename]
        else:
            sound = pygame.mixer.Sound(path.join(assets, filename))
            self.sounds[filename] = sound
            return self.sounds[filename]

    def add_sprite(self, sprite_component):
        draw_order = sprite_component.draw_order

        index = 0
        for sprite in self.sprites:
            if draw_order < sprite.draw_order:
                break
            index += 1

        self.sprites.insert(index, sprite_component)

    def remove_sprite(self, sprite_component):
        self.sprites = [
            sprite for sprite in self.sprites if sprite != sprite_component]

    def add_collider(self, collider):
        self.colliders.append(collider)

    def remove_collider(self, collider):
        try:
            self.colliders.remove(collider)
        except ValueError:
            pass

    def resume(self):
        self.is_paused = False

    def pause(self):
        self.is_paused = True

    def add_ui(self, ui_element):
        self.ui_elements.append(ui_element)
