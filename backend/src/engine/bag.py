from coord import Coord


class Bag:
    def __init__(self, size: Coord, mass_limit: int):
        self.size = size
        self.mass_limit = mass_limit
