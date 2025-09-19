"""
Implement a `Polynomial` class that:
- Stores coefficients in a list (lowest degree first).
- Implements `__call__` to evaluate at a given `x`.
- Supports polynomial addition and equality.
- Has a readable `__repr__` (e.g., `Polynomial(2x^2 + 3x + 1)`).


Example:
```python
>>> p1 = Polynomial([1, 3, 2]) # 2x² + 3x + 1
>>> p2 = Polynomial([0, 1]) # x
>>> print(p1(2)) # Evaluate at x=2 → 2*4 + 3*2 + 1 = 15
>>> print(p1 + p2) # Polynomial(2x^2 + 4x + 1)

"""

class Polynomial():
    pass