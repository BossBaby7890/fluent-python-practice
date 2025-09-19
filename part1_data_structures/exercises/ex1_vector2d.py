"""
Exercise 1: Vector2D

Implement a 2D vector class that supports:
- Addition and subtraction
- Scalar multiplication (v * 3 and 3 * v)
- Equality
- abs(v) → magnitude
- hash(v) so it can be used in sets and dict keys

Example:
>>> v1 = Vector2D(3, 4)
>>> v2 = Vector2D(1, 2)
>>> print(v1 + v2)   # Vector2D(4, 6)
>>> print(abs(v1))   # 5.0
"""
import math

class Vector2D:
    def __init__(self, x, y):
        """Initialize vector with x and y coordinates."""
        self.x = x
        self.y = y

    def __repr__(self):
        """Return string representation like Vector2D(3, 4)."""
        return f"Vector2D({self.x}, {self.y})"

    def __eq__(self, other):
        """Check vector equality."""
        return isinstance(other, Vector2D) and self.x == other.x and self.y == other.y

    def __add__(self, other):
        """Vector addition."""
        x = self.x + other.x
        y = self.y + other.y
        return Vector2D(x, y)

    def __sub__(self, other):
        """Vector subtraction."""
        x = self.x - other.x
        y = self.y - other.y
        return Vector2D(x, y)

    def __mul__(self, scalar):
        """Scalar multiplication: v * scalar."""
        x = self.x * scalar
        y = self.y * scalar
        return Vector2D(x, y)
        

    def __rmul__(self, scalar):
        """Scalar multiplication: scalar * v."""
        x = self.x * scalar
        y = self.y * scalar
        return Vector2D(x, y)

    def __abs__(self):
        """Return the magnitude of the vector."""
        return math.hypot(self.x, self.y)
 
    def __hash__(self):
        """Make the vector hashable."""
        return hash((self.x, self.y))


if __name__ == "__main__":
    # Quick test cases (to try after implementation)
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)

    print("v1:", v1)
    print("v2:", v2)
    print("v1 + v2:", v1 + v2)
    print("v1 - v2:", v1 - v2)
    print("v1 * 3:", v1 * 3)
    print("2 * v2:", 2 * v2)
    print("abs(v1):", abs(v1))
    print("Equality test:", v1 == Vector2D(3, 4))
    print("Hashable test:", {v1, v2})
