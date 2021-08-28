import numpy as np

from .arrangement import Arrangement
from .item import Item
from .coord import Coord


def value(policy: Arrangement):
    k1 = 5
    k2 = 1

    occupancy = policy.occupancy
    items = policy.items

    unsecured_items_cost = sum((x.get_mass()
                               for x in get_unsecured_items(occupancy, items)))

    val = - (k1 * get_vertical_void_area(occupancy) +
             k2 * unsecured_items_cost)
    print(val)
    return val


def get_vertical_void_area(occupancy):
    M = occupancy.copy()
    M[M > 0] = 1
    M = np.diff(M, axis=0)
    M[M == 1] = 0
    void_area = -np.sum(M)

    return void_area


def get_unsecured_items(occupancy, items):
    unsecured_items = []

    M = occupancy.copy()
    M[M > 0] = 1
    edge_change = np.diff(M, prepend=np.ones(
        (M.shape[1], 1), dtype=int), append=np.ones((M.shape[1], 1), dtype=int))

    for (item, item_id) in zip(items, range(1, len(items)+1)):
        M = occupancy.copy()

        item_mask = np.zeros(occupancy.shape, dtype=int)
        item_mask[occupancy == item_id] = 1
        # print(item_mask)
        # print(edge_change)

        # Check left
        masked = np.multiply(item_mask, edge_change[:, 0:-1])
        # print(masked)
        # print(np.sum(masked))
        if np.sum(masked) == item.size.y:
            unsecured_items.append(item)
            continue

        # Check right
        masked = np.multiply(item_mask, edge_change[:, 1:])
        # print(masked)
        # print(np.sum(masked))
        if np.sum(masked) == -item.size.y:
            unsecured_items.append(item)
            continue

    return unsecured_items


if __name__ == "__main__":
    # M = np.array([[1, 0, 0], [1, 0, 0], [1, 0, 0]])
    # print(get_unsecured_items(M, [Item(Coord(1, 3), 0, 0)]))
    # print("\n===\n")
    # M = np.array([[1, 0, 0], [1, 0, 0], [1, 2, 2]])
    # get_unsecured_items(M, [Item(Coord(1, 3), 0, 0), Item(Coord(2, 1), 0, 0)])
    # print("\n===\n")
    # M = np.array([[0, 0, 0], [0, 0, 1], [0, 0, 1]])
    # i = get_unsecured_items(M, [Item(Coord(1, 2), 0, 0)])
    # print(i)

    # M = np.array([[3, 0, 0], [3, 0, 0], [1, 2, 2]])
    # i = get_unsecured_items(M, [Item(Coord(1, 1), 0, 0), Item(Coord(2, 1), 0, 0), Item(Coord(1, 2), 0, 0)])
    # print(i)
    pass
