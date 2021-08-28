from .coord import Coord


class Item:
    def __init__(self, size: Coord, mass_density: int, strength: int):
        self.size = size
        self.mass_density = mass_density
        self.strength = strength

    def get_area(self):
        return self.size.x * self.size.y

    def get_mass(self):
        return self.get_area() * self.mass_density

    def get_inverse(self):
        return Item(Coord(self.size.y, self.size.x), self.mass_density, self.strength)
