import unittest

from .coord import Coord
from .item import Item


class TestItem(unittest.TestCase):
    def test_create_item(self):
        item = Item(Coord(2, 3), 3, 5)

    def test_item_mass(self):
        item = Item(Coord(2, 3), 3, 5)
        self.assertEqual(2 * 3 * 3, item.get_mass())
