import pygame
from actors.actor import Actor

class Game:
    def initialize(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500,500))
        self.ticksCount = 0
        self.is_running = True
        self.actors = [Actor(10,10)]
        self.horizontalAxis = 0

    def shutdown(self):
        print("Shutting down game")
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
        deltaTime = (pygame.time.get_ticks() - self.ticksCount) / 1000
        self.ticksCount = pygame.time.get_ticks()

        for actor in self.actors:
            actor.update(deltaTime, self.horizontalAxis)

    def render(self):
        self.screen.fill((50, 0, 0))
        for actor in self.actors:
            actor.render(self.screen)
    