
from .arrangement_generator import Timer, generate_arrangements_parallelised
from .arrangement import Arrangement
from .bag import Bag
from .coord import Coord
from .item import Item
from .valuation import value

if __name__ == '__main__':
    items = [
        Item(Coord(4, 4), 1, 1),
        Item(Coord(2, 6), 1, 1),
        Item(Coord(2, 3), 1, 1),
        # Item(Coord(8, 8), 1, 1),
        # Item(Coord(7, 3), 1, 1),
        # Item(Coord(2, 8), 1, 1),
        # Item(Coord(1, 4), 1, 1),
        # Item(Coord(4, 3), 1, 1),
        # Item(Coord(2, 2), 1, 1),
    ]

    bag = Bag(Coord(7, 7), 1000)

    with Timer("Parallelised"):
        arrangements = generate_arrangements_parallelised(bag, items)

    # with Timer("Not parallelised"):
    #     res = generate_arrangements(bag, items)

    count = 0

    for i, arrangement in enumerate(arrangements):
        # arrangement.display()
        print(str(arrangement))
        arrangement.value = value(arrangement)

        count += 1

    arrangements.sort(key=lambda x: x.value, reverse=True)

    # best = arrangements[0]
    # best.display()

    for i, a in enumerate(arrangements):
        a.display_save(str(i))
        # a.display()
