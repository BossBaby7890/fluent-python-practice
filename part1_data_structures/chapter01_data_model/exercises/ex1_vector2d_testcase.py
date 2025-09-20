import pytest

from ex1_vector2d import Vector2D

def test_addition_and_subtraction():
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)
    assert v1 + v2 == Vector2D(4, 6)
    assert v1 - v2 == Vector2D(2, 2)

def test_scalar_multiplication():
    v = Vector2D(2, -3)
    assert v * 3 == Vector2D(6, -9)
    assert 4 * v == Vector2D(8, -12)

def test_abs_and_len():
    v = Vector2D(3, 4)
    assert abs(v) == 5.0
    assert len(v) == 2

def test_equality_and_hashability():
    v1 = Vector2D(1, 1)
    v2 = Vector2D(1, 1)
    v3 = Vector2D(2, 2)
    assert v1 == v2
    assert v1 != v3
    s = {v1, v2, v3}
    assert len(s) == 2  # v1 and v2 are equal, v3 is different

def test_repr_contains_coordinates():
    v = Vector2D(7, -5)
    r = repr(v)
    assert "Vector2D" in r
    assert "7" in r
    assert "-5" in r
