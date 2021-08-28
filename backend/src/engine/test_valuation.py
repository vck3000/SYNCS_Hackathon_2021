import unittest

import numpy as np

from .valuation import *


class TestVerticalVoid(unittest.TestCase):
    pass


class TestUnsecuredItems(unittest.TestCase):

    def test_simple_unsecured(self):
        M = np.array([[1, 0, 0], [1, 0, 0], [1, 0, 0]])
        self.assertTrue(get_unsecured_items(M, [1]))
