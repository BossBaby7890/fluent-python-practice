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
        return f"PixelGrid({self.width}x{self.height})"

    def __getitem__(self, idx):
        y , x = idx
        return self.grid[x][y]

    def __setitem__(self, idx, value):
        y , x = idx
        self.grid[x][y] = value

    def __len__(self):
        return len(self.grid)



