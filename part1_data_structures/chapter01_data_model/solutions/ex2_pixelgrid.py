class PixelGrid:
    def __init__(self, width, height, default=(0, 0, 0)):
        self.width = width
        self.height = height
        self.pixels = [[default for _ in range(width)] for _ in range(height)]


    def __getitem__(self, pos):
        row, col = pos
        return self.pixels[row][col]


    def __setitem__(self, pos, value):
        row, col = pos
        self.pixels[row][col] = value


    def __len__(self):
        return self.height


    def __repr__(self):
        preview = [row[:5] for row in self.pixels[:5]]
        return f"PixelGrid({self.width}x{self.height}, preview={preview})"