import unittest

from .bag import Bag
from .coord import Coord


class TestBag(unittest.TestCase):
    def test_create_bag(self):
        bag = Bag(Coord(5, 7), 10)
