"""
Create a class `PixelGrid` that:
- Represents a 2D image grid of pixels (width x height).
- Supports `__getitem__` and `__setitem__` for accessing/modifying pixels.
- Supports slicing rows or columns.
- Provides `__len__` to return the number of rows.
- Implements `__repr__` to display a small preview (e.g., 5x5 section).


Example:

>>> pg = PixelGrid(10, 10)
>>> pg[0, 0] = (255, 0, 0) # Set top-left pixel red
>>> print(pg[0, 0]) # (255, 0, 0)
>>> print(len(pg)) # 10

"""

class PixelGrid():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]


    def __repr__(self):
        pass

    def __getitem__(self):
        pass

    def __setitem__(self, idx, value):
        self.grid



import numpy as np 
a = np.array([[1,2,3], [2,3,4]])

# print(a.shape)

row = 2
col = 3
grid = [[1,2,3], [2,3,4]]

print(grid[1])

