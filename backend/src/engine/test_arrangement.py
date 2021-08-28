import unittest

from typing import List

from .arrangement import Arrangement
from .bag import Bag
from .coord import Coord
from .item import Item


class TestArrangement(unittest.TestCase):
    def setUp(self):
        self.bag = Bag(Coord(5, 5), 100)
        self.items = [Item(Coord(2, 3), 5, 10)]

    # Arrangement with no items
    def test_create_empty_arrangement(self):
        Arrangement(self.bag)

    # Arrangement with one valid item
    def test_create_arrangement_items(self):
        arrangement = Arrangement(self.bag)
        item = Item(Coord(2, 3),5,10)
        arrangement.add_item(item, Coord(0, 0))
        
        #TODO - write a nice function for testing many cells!
        self.assertEqual(arrangement.occupancy[0,0], id(item))
        self.assertEqual(arrangement.occupancy[0,1], id(item))
        self.assertEqual(arrangement.occupancy[0,2], id(item))
        self.assertNotEqual(arrangement.occupancy[0,3], id(item))

        self.assertEqual(arrangement.occupancy[1,0], id(item))
        self.assertEqual(arrangement.occupancy[1,1], id(item))
        self.assertEqual(arrangement.occupancy[1,2], id(item))
        self.assertNotEqual(arrangement.occupancy[1,3], id(item))

        self.assertNotEqual(arrangement.occupancy[2,0], id(item))
        self.assertNotEqual(arrangement.occupancy[2,1], id(item))
        self.assertNotEqual(arrangement.occupancy[2,2], id(item))
        self.assertNotEqual(arrangement.occupancy[2,3], id(item))

    # Helper function to create an arrangement with multiple items
    def create_arrangement_multiple(self, items: List[Item], locations: List[Coord]):
        arrangement = Arrangement(self.bag)

        for item, location in zip(items, locations):
            arrangement.add_item(item, location)

        return arrangement

    # Arrangement with two valid items
    def test_create_arrangement_multiple_items(self):

        item1 = Item(Coord(2, 2),5,10)
        item2 = Item(Coord(2, 2),5,10)
        items = [item1, item2]
        locations = [Coord(0,0), Coord(0, 3)]
        arrangement = self.create_arrangement_multiple(items, locations)

        self.assertEqual(arrangement.occupancy[0,0], id(item1))
        self.assertEqual(arrangement.occupancy[0,1], id(item1))
        self.assertEqual(arrangement.occupancy[0,2], 0)
        self.assertEqual(arrangement.occupancy[0,3], id(item2))
        self.assertEqual(arrangement.occupancy[0,4], id(item2))

        self.assertEqual(arrangement.occupancy[1,0], id(item1))
        self.assertEqual(arrangement.occupancy[1,1], id(item1))
        self.assertEqual(arrangement.occupancy[1,2], 0)
        self.assertEqual(arrangement.occupancy[1,3], id(item2))
        self.assertEqual(arrangement.occupancy[1,4], id(item2))

        self.assertEqual(arrangement.occupancy[2,0], 0)
        self.assertEqual(arrangement.occupancy[2,1], 0)
        self.assertEqual(arrangement.occupancy[2,2], 0)
        self.assertEqual(arrangement.occupancy[2,3], 0)
        self.assertEqual(arrangement.occupancy[2,4], 0)


    # Arrangement with items out of bounds
    def test_invalid_arrangement_out_of_bound(self):

        item = Item(Coord(2, 3),5,10)

        # Item way outside
        arrangement = Arrangement(self.bag)
        self.assertEqual(False, arrangement.add_item(item, Coord(10, 0)))

        # Item over the edge of bag
        arrangement = Arrangement(self.bag)
        self.assertEqual(False, arrangement.add_item(item, Coord(4, 0)))

        # Item on the edge of bag
        arrangement = Arrangement(self.bag)
        self.assertEqual(True, arrangement.add_item(item, Coord(3, 0)))

        # Item over the y edge of bag
        arrangement = Arrangement(self.bag)
        self.assertEqual(False, arrangement.add_item(item, Coord(0, 3)))

    # Verify that items are being added to the dictionary
    def test_dictionary_size(self):
        arrangement = Arrangement(self.bag)
        self.assertEqual(0, len(arrangement.items))

        item1 = Item(Coord(1, 3),5,10)
        arrangement.add_item(item1, Coord(0, 0))
        self.assertEqual(1, len(arrangement.items))

        item2 = Item(Coord(1, 2),5,10)
        arrangement.add_item(item2, Coord(1, 0))
        self.assertEqual(2, len(arrangement.items))

        item3 = Item(Coord(1, 2),5,10)
        arrangement.add_item(item3, Coord(2, 0))
        self.assertEqual(3, len(arrangement.items))

    def test_invalid_arrangement_mass(self):

        arrangement = Arrangement(self.bag)
        item1 = Item(Coord(1, 3),5,10)
        self.assertEqual(True, arrangement.add_item(item1, Coord(0, 0)))
        self.assertEqual(1*3*5, arrangement.mass_filled)

        item2 = Item(Coord(1, 2),500,10)
        self.assertEqual(False, arrangement.add_item(item2, Coord(1, 0)))
        self.assertEqual(1*3*5, arrangement.mass_filled)


    # def test_too_heavy(self):
    #     # 10kg bag is been given 30kg item
    #     bag = Bag(Coord(5, 5), 10)
    #     items = [Item(Coord(2, 3), 5, 10)]

    #     arrangement = Arrangement(bag, items, [Coord(0, 0)])
    #     self.assertEquals(False, arrangement.is_valid())

    # TODO

    # def test_item_overlap(self):
    #     bag = Bag(Coord(5, 5), 10)
    #     items = [Item(Coord(2, 3), 5, 10), Item(Coord(2, 3), 5, 10)]

    #     arrangement = Arrangement(bag, items, [Coord(0, 0), Coord(0, 0)])
    #     self.assertEquals(False, arrangement.is_valid())

        # Check x edge overlap

        # Diagonal positioning overlap (corner case) both just in and just out

        # Check y edge overlap

        # Location orientation
