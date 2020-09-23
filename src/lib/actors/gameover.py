import pygame
from .actor import Actor
from lib.ui.text import TextUI


class GameOver(Actor):
    def start(self):
        self.reference = 50
        self.is_gameover = False
        self.text_ui = TextUI(self.game)
        self.text_ui.text = ''
        self.game.add_ui(self.text_ui)

    def update_actor(self, delta_time):
        self.reference -= delta_time
        if self.reference <= 0 or self.is_gameover:
            self.text_ui.text = 'Game Over'
            self.game.pause()
