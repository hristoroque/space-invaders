class Vector2():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, vector2):
        return Vector2(
            self.x + vector2.x,
            self.y + vector2.y
            )

    def dot(self, vector2):
        return Vector2(
            self.x * vector2.x,
            self.y * vector2.y,
        )

    def times(self,scalar):
        return Vector2(
            self.x * scalar,
            self.y * scalar
        )
    
    def __mul__(self, scalar):
        return self.times(scalar)

    def __str__(self):
        return f'<{self.x},{self.y}>'