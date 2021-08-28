from bag import Bag


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

    def __init__(self, bag: Bag, items, locations):
        self.bag = bag
        self.items = items
        self.locations = locations

    def is_valid(self):
        for location in self.locations:
            if location[0] > self.bag.size[0]:
                return False

        return True
