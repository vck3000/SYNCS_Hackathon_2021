from typing import List

from .arrangement import Arrangement
from .bag import Bag
from .coord import Coord
from .item import Item


def generate_arrangements(bag: Bag, items: List[Item]):
    return generate_arrangements_recurse(items, Arrangement(bag))


def generate_arrangements_recurse(
    items: List[Item],
    arrangement: Arrangement,
) -> List[Arrangement]:
    if len(items) == 0:
        return [arrangement]

    valid_arrangements = []

    for item in items:
        for x in range(arrangement.bag.size.x):
            for y in range(arrangement.bag.size.y):
                new_arrangement = arrangement.clone()
                res = new_arrangement.add_item(item, Coord(x, y))

                if res == True:
                    valid_arrangements += generate_arrangements_recurse(
                        items[1:], new_arrangement
                    )

                # Repeat for inversed item
                new_arrangement = arrangement.clone()
                res = new_arrangement.add_item(item.get_inverse(), Coord(x, y))

                if res == True:
                    valid_arrangements += generate_arrangements_recurse(
                        items[1:], new_arrangement
                    )

    return valid_arrangements


if __name__ == "__main__":
    items = [
        Item(Coord(1, 2), 1, 1),
        Item(Coord(1, 3), 1, 1),
        Item(Coord(2, 3), 1, 1),
    ]

    bag = Bag(Coord(5, 5), 1000)

    res = generate_arrangements(bag, items)

    for arrangement in res:
        arrangement.display()
