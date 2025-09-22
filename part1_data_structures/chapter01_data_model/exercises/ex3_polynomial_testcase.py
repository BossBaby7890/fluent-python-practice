import pytest

from ex3_polynomial import Polynomial

def test_polynomial_evaluation():
    p = Polynomial([1, 3, 2])  # 2x² + 3x + 1
    assert p(2) == 15

def test_polynomial_addition():
    p1 = Polynomial([1, 3, 2])   # 2x² + 3x + 1
    p2 = Polynomial([0, 1])      # x
    result = p1 + p2
    assert result == Polynomial([1, 4, 2])

def test_polynomial_equality():
    p1 = Polynomial([1, 2, 3])
    p2 = Polynomial([1, 2, 3])
    p3 = Polynomial([1, 2])
    assert p1 == p2
    assert p1 != p3

def test_polynomial_repr():
    p = Polynomial([1, 3, 2])
    r = repr(p)
    assert "Polynomial" in r
    assert "2x^2" in r
