class Vector2():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, vector2):
        return Vector2(
            self.x + vector2.x,
            self.y + vector2.y
            )