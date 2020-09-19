from .base import Component

class SpriteComponent(Component):
    def __init__(self, actor, draw_order = 1):
        super().__init__(actor)
        self.draw_order = draw_order
        self.image = None
        self.height = 0
        self.width = 0
        self.actor.game.add_sprite(self)

    def set_image(self, image):
        self.image = image
        self.width, self.height = image.get_rect().size

    def draw(self, screen):
        screen.blit(self.image, (
            self.actor.position.x - self.width/2,
            self.actor.position.y - self.height/2
        ))