import pytest

from ex2_pixelgrid import PixelGrid

def test_pixel_assignment_and_retrieval():
    pg = PixelGrid(5, 5)
    pg[0, 0] = (255, 0, 0)
    assert pg[0, 0] == (255, 0, 0)

def test_len_returns_height():
    pg = PixelGrid(4, 6)
    assert len(pg) == 6

def test_repr_contains_dimensions():
    pg = PixelGrid(2, 2)
    r = repr(pg)
    assert "PixelGrid(2x2)" in r
