from .base import Component

class SpriteComponent(Component):
    def __init__(self, actor, draw_order = 1):
        super().__init__(actor)
        self.draw_order = draw_order
        self.image = None

    def set_image(self, image):
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, (
            self.actor.position.x,
            self.actor.position.y
        ))