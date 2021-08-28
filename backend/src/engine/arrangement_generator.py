from typing import List

from .arrangement import Arrangement
from .bag import Bag
from .coord import Coord
from .item import Item


import multiprocessing as mp
from multiprocessing import Pool
import numpy as np

import time


class Timer(object):
    def __init__(self, name=None):
        self.name = name

    def __enter__(self):
        self.tstart = time.time()

    def __exit__(self, type, value, traceback):
        if self.name:
            print(
                "[%s]" % self.name,
            )
        print("Elapsed: %s" % (time.time() - self.tstart))


def generate_arrangements(bag: Bag, items: List[Item]):
    return generate_arrangements_recurse(items, Arrangement(bag))


def generate_arrangements_parallelised(bag: Bag, items: List[Item]):
    num_processes = int(mp.cpu_count())
    if bag.size.x < num_processes:
        num_processes = bag.size.x

    print(f"Using {num_processes} cores.")

    pool = Pool(processes=num_processes)  # start 4 worker processes
    # result = pool.apply_async(f, [10])    # evaluate "f(10)" asynchronously
    # print result.get(timeout=1)           # prints "100" unless your computer is *very* slow

    items_mapped = [items for i in range(num_processes)]
    arrangements_mapped = [Arrangement(bag) for i in range(num_processes)]

    intervals = np.linspace(0, bag.size.x, num_processes + 1)
    intervals = list(map(lambda x: int(x), intervals))

    x_start_mapped = intervals[0:-1]
    x_end_mapped = intervals[1:]

    data_mapped = zip(items_mapped, arrangements_mapped, x_start_mapped, x_end_mapped)

    # print(list(data_mapped))

    result = pool.starmap(
        # generate_arrangements_recurse_parallelised,
        generate_arrangements_iterative_parallelised,
        data_mapped,
    )

    # [[sol1, sol2], [sol3, sol4]]
    # [sol1, sol2, sol3, sol4]

    return [item for sublist in result for item in sublist]


def generate_arrangements_iterative_parallelised(
    items_start: List[Item],
    arrangement_start: Arrangement,
    x_start_start: int,
    x_end_start: int,
) -> List[Arrangement]:

    valid_arrangements = []

    nodes = [(items_start, arrangement_start)]

    x_start = x_start_start
    x_end = x_end_start

    while True:
        if len(nodes) == 0:
            break

        items, arrangement = nodes.pop()

        if len(items) == 0:
            valid_arrangements += [arrangement]
            continue

        for x in range(x_start, x_end):
            for y in range(arrangement.bag.size.y):
                for i, item in enumerate(items):
                    new_arrangement = arrangement.clone()
                    res = new_arrangement.add_item(item, Coord(x, y))

                    if res == True:
                        nodes.append((items[:i] + items[i + 1 :], new_arrangement))

                    # Repeat for inversed item
                    new_arrangement = arrangement.clone()
                    res = new_arrangement.add_item(item.get_inverse(), Coord(x, y))

                    if res == True:
                        nodes.append((items[:i] + items[i + 1 :], new_arrangement))

            # After first block is placed, x now spans anywhere across the x axis
            x_start = 0
            x_end = arrangement.bag.size.x

    # Optional matplotlib savefig
    # for i, arrangement in enumerate(valid_arrangements):
    #     arrangement.display_save(f"{x_start_start}_{i}")
    #     print(f"{x_start_start}_{i}")

    return valid_arrangements


def generate_arrangements_recurse_parallelised(
    items: List[Item],
    arrangement: Arrangement,
    x_start: int,
    x_end: int,
) -> List[Arrangement]:
    if len(items) == 0:
        return [arrangement]

    valid_arrangements = []

    for x in range(x_start, x_end):
        for y in range(arrangement.bag.size.y):
            for i, item in enumerate(items):
                new_arrangement = arrangement.clone()
                res = new_arrangement.add_item(item, Coord(x, y))

                if res == True:
                    valid_arrangements += generate_arrangements_recurse(
                        items[:i] + items[i + 1 :], new_arrangement
                    )

                # Repeat for inversed item
                new_arrangement = arrangement.clone()
                res = new_arrangement.add_item(item.get_inverse(), Coord(x, y))

                if res == True:
                    valid_arrangements += generate_arrangements_recurse(
                        items[:i] + items[i + 1 :], new_arrangement
                    )

    # Optional matplotlib savefig
    # for i, arrangement in enumerate(valid_arrangements):
    #     arrangement.display_save(f"{x_start}_{i}")
    #     print(f"{x_start}_{i}")

    return valid_arrangements


def generate_arrangements_recurse(
    items: List[Item],
    arrangement: Arrangement,
) -> List[Arrangement]:
    if len(items) == 0:
        return [arrangement]

    valid_arrangements = []

    for x in range(arrangement.bag.size.x):
        for y in range(arrangement.bag.size.y):
            for i, item in enumerate(items):
                new_arrangement = arrangement.clone()
                res = new_arrangement.add_item(item, Coord(x, y))

                if res == True:
                    valid_arrangements += generate_arrangements_recurse(
                        items[:i] + items[i + 1 :], new_arrangement
                    )

                # Repeat for inversed item
                new_arrangement = arrangement.clone()
                res = new_arrangement.add_item(item.get_inverse(), Coord(x, y))

                if res == True:
                    valid_arrangements += generate_arrangements_recurse(
                        items[:i] + items[i + 1 :], new_arrangement
                    )

    return valid_arrangements


if __name__ == "__main__":
    items = [
        Item(Coord(2, 4), 1, 1),
        Item(Coord(2, 6), 1, 1),
        Item(Coord(4, 6), 1, 1),
        # Item(Coord(8, 8), 1, 1),
        # Item(Coord(7, 3), 1, 1),
        # Item(Coord(2, 8), 1, 1),
        # Item(Coord(1, 4), 1, 1),
        # Item(Coord(4, 3), 1, 1),
        # Item(Coord(2, 2), 1, 1),
    ]

    bag = Bag(Coord(16, 16), 1000)

    with Timer("Parallelised"):
        res = generate_arrangements_parallelised(bag, items)

    # with Timer("Not parallelised"):
    #     res = generate_arrangements(bag, items)

    count = 0
    for i, arrangement in enumerate(res):
        # arrangement.display()
        # arrangement.display_save(str(i))
        # print(str(arrangement))

        # print(count)

        count += 1

    print(count)
