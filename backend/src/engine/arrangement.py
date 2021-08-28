from typing import List
import numpy as np
import matplotlib.pyplot as plt

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
        self.bag = bag          # The bag
        self.items = dict()     # Dictionary of items in the bag
        self.mass_filled = 0    # Mass of items in the bag

        # Create occupancy matrix with bag dimensions
        self.occupancy = np.zeros((bag.size.x, bag.size.y), dtype=int)

    # Add an item at the given coordinate
    # Return false if placing this item would violate imposed conditions
    # Return true otherwise
    def add_item(self, item: Item, location: Coord):

        #TODO: make checks into separate function
        # Check item bounds
        if location.x + item.size.x > self.bag.size.x:
            return False

        if location.y + item.size.y > self.bag.size.y:
            return False

        # Check bag max weight limit not exceeded
        if self.mass_filled + item.get_mass() > self.bag.mass_limit:
            return False

        # Check occupancy grid vacant
        for x in range(location.x, location.x + item.size.x):
            for y in range(location.y, location.y + item.size.y):
                if(self.occupancy[x, y] != 0):
                    return False

        #TODO: make add steps into separate function
        #! Should not add unless all checks passed! 
        # Place in occupancy grid
            for x in range(location.x, location.x + item.size.x):
                for y in range(location.y, location.y + item.size.y):
                    # Assign corresponding occupancy grid square the value of the item's id
                    self.occupancy[x, y] = id(item)

        # Increment mass
        self.mass_filled += item.get_mass()

        # Store in dictionary
        self.items[id(item)] = item
        return True


    # Plot with matplotlib
    def display(self):

        data = self.occupancy

        # Replace big id values in matrix with integers 1, 2, 3... etc so that heat map scales nicely
        for key, index in zip(self.items, range(len(self.items))):
            data = np.where(data == key, index+1, data)

        plt.imshow(data, cmap='hot_r', origin='lower')
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Arrangement")
        plt.show()


    # def is_valid(self):
    #     

    #     # Add up all item weights and ensure not exceeding bag
    #     net_mass = 0
    #     for item in self.items:
    #         net_mass += item.get_mass()

    #     if net_mass > self.bag.mass_limit:
    #         return False

    #     return True
