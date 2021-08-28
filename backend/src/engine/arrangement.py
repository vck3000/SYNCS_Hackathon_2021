from typing import List
import numpy as np
import matplotlib.pyplot as plt

from .bag import Bag
from .coord import Coord
from .item import Item


class Arrangement:
    """An arrangement is a solution.

    np.array[y,x]
    ---------------
    |[n,0]   [n,n]|
    |             |
    |             |
    |             |
    |[0,0]   [0,n]|
    ---------------
    """

    def __init__(self, bag: Bag):
        self.bag = bag  # The bag
        self.mass_filled = 0  # Mass of items in the bag

        # Create occupancy matrix with bag dimensions
        self.occupancy = np.zeros((bag.size.x, bag.size.y), dtype=int)

        self.items = []
        self.locations = []

        self.counter = 1

    def clone(self):
        clone = Arrangement(self.bag)

        for item, location in zip(self.items, self.locations):
            clone.add_item(item, location)

        return clone

    # Add an item at the given coordinate
    # Return false if placing this item would violate imposed conditions
    # Return true otherwise
    def add_item(self, item: Item, location: Coord):

        # TODO: make checks into separate function
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
                if self.occupancy[y, x] != 0:
                    return False

        # Check floating
        floating = False if location.y == 0 else True
        if location.y != 0:
            for x in range(location.x, location.x + item.size.x):
                # If any of the below cells are filled
                if self.occupancy[location.y - 1, x] != 0:
                    floating = False

        if floating:
            return False

        # TODO: make add steps into separate function
        #! Should not add unless all checks passed!
        # Place in occupancy grid
        for x in range(location.x, location.x + item.size.x):
            for y in range(location.y, location.y + item.size.y):
                # Assign corresponding occupancy grid square the value of the item's id
                self.occupancy[y, x] = self.counter

        # Increment mass
        self.mass_filled += item.get_mass()

        self.items.append(item)
        self.locations.append(location)

        self.counter += 1

        return True

    # Plot with matplotlib

    def display(self):
        data = self.occupancy

        plt.imshow(data, cmap="hot_r", origin="lower", vmin=0, vmax=len(self.items) + 1)
        plt.colorbar()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Arrangement")
        plt.show()

    def display_save(self, name):
        data = self.occupancy

        plt.clf()
        plt.imshow(data, cmap="hot_r", origin="lower", vmin=0, vmax=len(self.items) + 1)
        plt.colorbar()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Arrangement")

        plt.savefig(f"./output/{name}.png")

    def __str__(self):
        outputStr = "Locations: \n"

        for location in self.locations:
            outputStr += str(location) + "\n"

        return outputStr

    # def is_valid(self):
    #

    #     # Add up all item weights and ensure not exceeding bag
    #     net_mass = 0
    #     for item in self.items:
    #         net_mass += item.get_mass()

    #     if net_mass > self.bag.mass_limit:
    #         return False

    #     return True
