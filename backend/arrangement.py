from coord import Coord
from item import Item
from bag import Bag
from typing import List


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
        for location in self.locations:
            if location.x > self.bag.size.x:
                return False

        return True
