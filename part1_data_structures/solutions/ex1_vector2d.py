import math


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"


    def __eq__(self, other):
        return isinstance(other, Vector2D) and self.x == other.x and self.y == other.y


    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)


    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)


    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)


    def __rmul__(self, scalar):
        return self.__mul__(scalar)


    def __abs__(self):
        return math.hypot(self.x, self.y)


    def __len__(self):
        return 2


    def __hash__(self):
        return hash((self.x, self.y))