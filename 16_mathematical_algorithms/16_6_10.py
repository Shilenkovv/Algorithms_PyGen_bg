from math import gcd
from typing import Tuple


def count_integer_points(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    return gcd(p2[1] - p1[1], p2[0] - p1[0]) + 1


# print(count_integer_points((2, 1), (6, 3)))
