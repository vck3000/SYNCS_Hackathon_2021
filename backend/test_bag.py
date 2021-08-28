import unittest

from bag import Bag


class TestBag(unittest.TestCase):
    def test_create_bag(self):
        bag = Bag((5, 7), 10)
