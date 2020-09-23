from .base import UIElement
from lib.vectors import Vector2


class TextUI(UIElement):
    def start(self):
        self.text = ''
        self.position = Vector2(
            self.game.width/2,
            self.game.height/2)

    def draw(self, screen):
        font = self.game.font.render(self.text, True, (255, 255, 255))
        width, height = self.game.font.size(self.text)
        screen.blit(font, (
            self.position.x - width/2, self.position.y - height/2)
        )
