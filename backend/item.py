class Item:
    def __init__(self, size, mass_density, strength):
        self.size = size
        self.mass_density = mass_density
        self.strength = strength

    def get_mass(self):
        return self.size.x * self.size.y * self.mass_density
