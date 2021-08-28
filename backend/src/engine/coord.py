class Coord:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    # def get_inverse()

    def __str__(self):
        return f"Coord x: {self.x}, y: {self.y}"
