import unittest

from coord import Coord
from item import Item
from bag import Bag
from arrangement import Arrangement


class TestArrangement(unittest.TestCase):
    def setUp(self):
        self.bag = Bag(Coord(5, 5), 10)
        self.items = [Item(Coord(2, 3), 5, 10)]

    def test_create_arrangement(self):
        locations = [Coord(0, 0)]

        arrangement = Arrangement(self.bag, self.items, locations)

    def test_valid_arrangement(self):
        locations = [Coord(0, 0)]

        arrangement = Arrangement(self.bag, self.items, locations)

        self.assertEquals(True, arrangement.is_valid())

    def test_invalid_arrangement(self):
        locations = [Coord(10, 0)]

        arrangement = Arrangement(self.bag, self.items, locations)

        self.assertEquals(False, arrangement.is_valid())
