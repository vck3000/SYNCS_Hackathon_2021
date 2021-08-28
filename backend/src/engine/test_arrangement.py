import unittest

from .arrangement import Arrangement
from .bag import Bag
from .coord import Coord
from .item import Item


class TestArrangement(unittest.TestCase):
    def setUp(self):
        self.bag = Bag(Coord(5, 5), 100)
        self.items = [Item(Coord(2, 3), 5, 10)]

    def create_simple_arrangement(self, itemSize: Coord, location: Coord):
        return Arrangement(self.bag, [Item(itemSize, 5, 10)], [location])

    def test_create_arrangement(self):
        self.create_simple_arrangement(Coord(2, 3), Coord(0, 0))

    def test_valid_arrangement(self):
        arrangement = self.create_simple_arrangement(Coord(2, 3), Coord(0, 0))
        self.assertEquals(True, arrangement.is_valid())

    def test_invalid_arrangement_x_out_of_bound(self):
        # Item way outside
        arrangement = self.create_simple_arrangement(Coord(2, 3), Coord(10, 0))
        self.assertEquals(False, arrangement.is_valid())

        # Item over the edge of bag
        arrangement = self.create_simple_arrangement(Coord(2, 3), Coord(4, 0))
        self.assertEquals(False, arrangement.is_valid())

        # Item on the edge of bag
        arrangement = self.create_simple_arrangement(Coord(2, 3), Coord(3, 0))
        self.assertEquals(True, arrangement.is_valid())

        # Item over the y edge of bag
        arrangement = self.create_simple_arrangement(Coord(2, 3), Coord(0, 3))
        self.assertEquals(False, arrangement.is_valid())

    def test_too_heavy(self):
        # 10kg bag is been given 30kg item
        bag = Bag(Coord(5, 5), 10)
        items = [Item(Coord(2, 3), 5, 10)]

        arrangement = Arrangement(bag, items, [Coord(0, 0)])
        self.assertEquals(False, arrangement.is_valid())

    # TODO

    def test_item_overlap(self):
        bag = Bag(Coord(5, 5), 10)
        items = [Item(Coord(2, 3), 5, 10), Item(Coord(2, 3), 5, 10)]

        arrangement = Arrangement(bag, items, [Coord(0, 0), Coord(0, 0)])
        self.assertEquals(False, arrangement.is_valid())

        # Check x edge overlap

        # Diagonal positioning overlap (corner case) both just in and just out

        # Check y edge overlap

        # Location orientation
