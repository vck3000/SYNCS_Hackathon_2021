import unittest

from coord import Coord
from bag import Bag


class TestBag(unittest.TestCase):
    def test_create_bag(self):
        bag = Bag(Coord(5, 7), 10)
