from .arrangement import Arrangement


def value(policy: Arrangement):
    height = policy.get_max_item_height()
    void_area = policy.get_void_area()
    

