from coord import Coord
from item import Item
from bag import Bag
from typing import List

from functools import reduce


class Arrangement:
    """An arrangement is a solution.

    ---------------
    |(n,0)   (n,n)|
    |             |
    |             |
    |             |
    |(0,0)   (0,n)|
    ---------------
    """

    def __init__(self, bag: Bag, items: List[Item], locations: List[Coord]):
        self.bag = bag
        self.items = items
        self.locations = locations

    def is_valid(self):
        # Check item bounds
        for item, location in zip(self.items, self.locations):
            if location.x + item.size.x > self.bag.size.x:
                return False

            if location.y + item.size.y > self.bag.size.y:
                return False

        # Add up all item weights and ensure not exceeding bag
        net_mass = 0
        for item in self.items:
            net_mass += item.get_mass()

        if net_mass > self.bag.mass_limit:
            return False

        return True
