import unittest

from .arrangement import Arrangement
from .bag import Bag
from .coord import Coord
from .item import Item
from .solvers import Solver


class BasicExperiments(unittest.TestCase):

    def test_no_items(self):
        bag = Bag(Coord(5, 5), 100)
        items = []

        arrangement = Arrangement(bag)
        solver = Solver(arrangement, items,
                        (Solver.STRONGEST_FIRST, Solver.BOTTOM_LEFT_FIRST))

        self.assertTrue(solver.run())

    def test_no_solution(self):
        bag = Bag(Coord(5, 5), 100)
        items = [Item(Coord(6, 6), 1, 10)]

        arrangement = Arrangement(bag)
        solver = Solver(arrangement, items,
                        (Solver.STRONGEST_FIRST, Solver.BOTTOM_LEFT_FIRST))

        self.assertFalse(solver.run())

    def test_perfect_fit(self):
        bag = Bag(Coord(5, 5), 100)
        items = [Item(Coord(5, 5), 1, 10)]

        arrangement = Arrangement(bag)
        solver = Solver(arrangement, items,
                        (Solver.STRONGEST_FIRST, Solver.BOTTOM_LEFT_FIRST))

        self.assertTrue(solver.run())
