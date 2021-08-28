import unittest

from .coord import Coord


class TestCoord(unittest.TestCase):
    def test_create_coord(self):
        coord = Coord(2, 3)
