from item import Item
from bag import Bag
import unittest

from arrangement import Arrangement


class TestArrangement(unittest.TestCase):
    def test_create_arrangement(self):
        bag = Bag((5, 5), 10)
        items = [Item((2, 3), 5, 10)]

        locations = [(0, 0)]

        arrangement = Arrangement(bag, items, locations)

    def test_valid_arrangement(self):
        bag = Bag((5, 5), 10)
        items = [Item((2, 3), 5, 10)]

        locations = [(0, 0)]

        arrangement = Arrangement(bag, items, locations)

        self.assertEquals(True, arrangement.is_valid())

    def test_invalid_arrangement(self):
        bag = Bag((5, 5), 10)
        items = [Item((2, 3), 5, 10)]

        locations = [(10, 0)]

        arrangement = Arrangement(bag, items, locations)

        self.assertEquals(False, arrangement.is_valid())
