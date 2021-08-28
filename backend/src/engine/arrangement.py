from typing import List
import numpy as np

from .bag import Bag
from .coord import Coord
from .item import Item


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

    def __init__(self, bag: Bag):
        self.bag = bag

        # Create occupancy matrix with bag dimensions
        self.occupancy = np.zeros((bag.size.x, bag.size.y), dtype=int)

    def add_item(self, item: Item, location: Coord):

        # Iterate over x and y values
        for x in range(location.x, location.x + item.size.x):
            for y in range(location.y, location.y + item.size.y):

                # Assign corresponding occupancy grid square the value of the item's id
                self.occupancy[x, y] = id(item)

    # def is_valid(self):
    #     # Check item bounds
    #     for item, location in zip(self.items, self.locations):
    #         if location.x + item.size.x > self.bag.size.x:
    #             return False

    #         if location.y + item.size.y > self.bag.size.y:
    #             return False

    #     # Add up all item weights and ensure not exceeding bag
    #     net_mass = 0
    #     for item in self.items:
    #         net_mass += item.get_mass()

    #     if net_mass > self.bag.mass_limit:
    #         return False

    #     return True
