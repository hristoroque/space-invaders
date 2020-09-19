from lib.actors.fire import Fire
from lib.vectors import Vector2
import math
# Implementing the strategy pattern for the shotting 😈

class ShootingStrategy():
    def shoot(self, game):
        pass

class SimpleShootStrategy(ShootingStrategy):
    def shoot(self, actor):
        game = actor.game
        fire = Fire(game)
        fire.position = Vector2(actor.position.x, actor.position.y)
        game.add_actor(fire)

class MultipleShootStrategy(ShootingStrategy):
    def shoot(self, actor):
        game = actor.game
        fires = [Fire(game), Fire(game), Fire(game)]
        fires[0].rotation = math.radians(90)
        fires[1].rotation = math.radians(100)
        fires[2].rotation = math.radians(80)

        for fire in fires:
            fire.position = Vector2(actor.position.x, actor.position.y)
            game.add_actor(fire)
        
        