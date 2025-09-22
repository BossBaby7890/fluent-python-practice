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
    def __init__(self, coefs):
        self.coefs = coefs
        self.order = len(self.coefs) if self.coefs[0]!= 0 else 1
    
    def __repr__(self):
        variables = ["" if i ==0 else "x" if i == 1 else f"x^{i}" for i in range(self.order)]
        expression = [f"{coeff}{vari}" for coeff, vari in zip(self.coefs, variables)]
        final_expression = "+".join(expression)
        return f"Polynomial(" + final_expression + ")"
    
    def __call__(self, x):
        y = 0
        for i in range(self.order):
            y += self.coefs[i] * (x**i)
        return y
    
    def __add__(self, other):
        max_order = max(self.order, other.order)

        self_padded = self.coefs + [0] * (max_order - self.order)
        other_padded = other.coefs + [0] * (max_order - other.order)

        total = [x + y for x, y in zip(self_padded, other_padded)]

        return Polynomial(total)
    
    def __eq__(self, other):
        return isinstance(other, Polynomial) and self.coefs == other.coefs

