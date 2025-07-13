from math import gcd
from typing import List, Tuple


def all_integer_points(p1: Tuple[int, int], p2: Tuple[int, int]) -> List[Tuple[int, int]]:
    cur_gcd = gcd(abs(p2[0] - p1[0]), abs(p2[1] - p1[1]))
    tot_points = cur_gcd + 1
    if tot_points == 2:
        return [p1, p2]

    step_x = (p2[0] - p1[0]) // cur_gcd
    step_y = (p2[1] - p1[1]) // cur_gcd

    ans: List[Tuple[int, int]] = []
    for i in range(tot_points):
        ans.append((p1[0] + step_x * i, p1[1] + step_y * i))

    return ans


# print(all_integer_points((0, 0), (6, 3)))  # [(0, 0), (2, 1), (4, 2), (6, 3)]
# print(all_integer_points((2, 6), (5, 2)))  # [(2, 6), (5, 2)]
# print(all_integer_points((3, 6), (6, 3)))  # [(3, 6), (4, 5), (5, 4), (6, 3)]
# print(all_integer_points((2, 8), (10, 4)))  # [(2, 8), (4, 7), (6, 6), (8, 5), (10, 4)]
