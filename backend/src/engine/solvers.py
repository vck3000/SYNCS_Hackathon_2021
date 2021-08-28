from .coord import Coord
from .item import Item
from .bag import Bag
from .arrangement import Arrangement

from typing import List, Tuple
from enum import Enum


class Solver:

    def __init__(self, arrangement: Arrangement, items: List[Item], strategies: Tuple[int]):
        self.arrangement = arrangement
        self.items = items
        self.placement_order_strategy = strategies[0]
        self.placement_strategy = strategies[0]

        self.sorted_items = self.get_placement_order(
            items, self.placement_order_strategy)

    def run(self):
        placed_item_count = 0
        while len(self.sorted_items) > 0:
            current_item = self.sorted_items.pop()
            isSuccessful = self.place_item(
                self.arrangement, current_item, self.placement_strategy)

            if not isSuccessful:
                print(
                    f"After placing {placed_item_count} items, unable to place next item: {current_item}")
                return False

            placed_item_count += 1

        print(f"Solver ran successfully, placed {placed_item_count} items")
        return True

    # Item placement order strategy
    STRONGEST_FIRST = 1
    DENSEST_FIRST = 2
    BIGGEST_FIRST = 3

    def get_placement_order(self, items: List[Item], strategy: int) -> List[Item]:
        if strategy == self.STRONGEST_FIRST:
            def sort_key(item): return item.strength
        elif strategy == self.DENSEST_FIRST:
            def sort_key(item): return item.mass_density
        elif strategy == self.BIGGEST_FIRST:
            def sort_key(item): return item.get_area()
        else:
            raise NotImplementedError

        sorted_items = sorted(items, key=sort_key, reverse=False)
        return sorted_items

    # Item placement strategy
    BOTTOM_LEFT_FIRST = 1
    BOTTOM_SIDE_FIRST = 2

    # Place item from bottom left, go up only when cant place items on row
    def place_item(self, state: Arrangement, item: Item, strategy: int):
        bag_width = state.bag.size.x
        bag_height = state.bag.size.y

        if strategy == self.BOTTOM_LEFT_FIRST:
            for y in range(bag_height):
                for x in range(bag_width):
                    isSuccessful = state.add_item(item, Coord(x, y))
                    if isSuccessful:
                        return True
        else:
            raise NotImplementedError

        return False
