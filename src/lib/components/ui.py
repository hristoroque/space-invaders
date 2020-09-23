from .base import Component


class TextUI(Component):
    def start(self, text):
        self.text = text

    def draw(self, screen):
        screen.blit(
            text,

        )
