import unittest

from .arrangement import Arrangement
from .bag import Bag
from .coord import Coord
from .item import Item
from .solvers import Solver


# class SingleItemExperiments(unittest.TestCase):
#     def test_fit(self):
#         bag = Bag(Coord(5, 5), 100)
#         items = [Item(Coord(1, 2), 1, 10)]

#         arrangement = Arrangement(bag)
#         solver = Solver(
#             arrangement, items, (Solver.STRONGEST_FIRST, Solver.BOTTOM_LEFT_FIRST)
#         )

#         self.assertTrue(solver.run())
#         # arrangement.display()

#     def test_fit_perfect(self):
#         bag = Bag(Coord(5, 5), 100)
#         items = [Item(Coord(5, 5), 1, 10)]

#         arrangement = Arrangement(bag)
#         solver = Solver(
#             arrangement, items, (Solver.STRONGEST_FIRST, Solver.BOTTOM_LEFT_FIRST)
#         )

#         self.assertTrue(solver.run())
#         # arrangement.display()

#     def test_no_items(self):
#         bag = Bag(Coord(5, 5), 100)
#         items = []

#         arrangement = Arrangement(bag)
#         solver = Solver(
#             arrangement, items, (Solver.STRONGEST_FIRST, Solver.BOTTOM_LEFT_FIRST)
#         )

#         self.assertTrue(solver.run())
#         # arrangement.display()

#     def test_no_solution(self):
#         bag = Bag(Coord(5, 5), 100)
#         items = [Item(Coord(6, 6), 1, 10)]

#         arrangement = Arrangement(bag)
#         solver = Solver(
#             arrangement, items, (Solver.STRONGEST_FIRST, Solver.BOTTOM_LEFT_FIRST)
#         )

#         self.assertFalse(solver.run())
#         # arrangement.display()


# class DoubleItemExperiments(unittest.TestCase):
#     def test_fit_right_adjacent(self):
#         bag = Bag(Coord(5, 5), 100)
#         items = [Item(Coord(1, 2), 1, 10), Item(Coord(2, 1), 1, 10)]

#         arrangement = Arrangement(bag)
#         solver = Solver(
#             arrangement, items, (Solver.STRONGEST_FIRST, Solver.BOTTOM_LEFT_FIRST)
#         )

#         self.assertTrue(solver.run())
#         # arrangement.display()

#     def test_fit_strongest_first_sorting(self):
#         bag = Bag(Coord(5, 5), 100)
#         items = [Item(Coord(1, 2), 1, 1), Item(Coord(2, 1), 1, 10)]

#         arrangement = Arrangement(bag)
#         solver = Solver(
#             arrangement, items, (Solver.STRONGEST_FIRST, Solver.BOTTOM_LEFT_FIRST)
#         )

#         self.assertTrue(solver.run())
#         self.assertEqual(arrangement.occupancy[0, 0], arrangement.occupancy[0, 1])
#         self.assertNotEqual(arrangement.occupancy[0, 0], arrangement.occupancy[1, 0])
#         # arrangement.display()

#     # def test_fit_strongest_first_counterexample(self):
#     #     bag = Bag(Coord(5, 5), 100)
#     #     items = [Item(Coord(2, 1), 1, 11), Item(Coord(5, 1), 1, 10)]

#     #     arrangement = Arrangement(bag)
#     #     solver = Solver(
#     #         arrangement, items, (Solver.STRONGEST_FIRST, Solver.BOTTOM_LEFT_FIRST)
#     #     )

#     #     self.assertTrue(solver.run())
#     #     # # self.assertEqual(
#     #     #     arrangement.occupancy[0, 0], arrangement.occupancy[1, 0])
#     #     # self.assertNotEqual(
#     #     #     arrangement.occupancy[0, 0], arrangement.occupancy[0, 1])
#     #     # arrangement.display()

#     # def test_fit_strongest_first_counterexample(self):
#     #     bag = Bag(Coord(3, 3), 100)
#     #     items = [Item(Coord(2, 1), 1, 11), Item(Coord(5, 1), 1, 10), Item]

#     #     arrangement = Arrangement(bag)
#     #     solver = Solver(
#     #         arrangement, items, (Solver.STRONGEST_FIRST, Solver.BOTTOM_LEFT_FIRST)
#     #     )

#     #     self.assertTrue(solver.run())
#     #     # arrangement.display()

