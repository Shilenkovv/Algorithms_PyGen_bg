from typing import List


def count_quadruplets_with_sum(nums: List[int], k: int) -> int:
    from itertools import combinations

    """
    Counts the maximum number of distinct quadruplets from the list `nums`
    such that the sum of each quadruplet is equal to `k`.

    :param nums: List of integers
    :param k: Target sum
    :return: Number of distinct quadruplets with sum equal to `k`
    """
    quadruplets = set()

    # Generate all quadruplets using combinations
    for quadruplet in combinations(nums, 4):
        if sum(quadruplet) == k:
            quadruplets.add(tuple(sorted(quadruplet)))

    return len(quadruplets)


# # Examples
# nums = [-2, 2, -1, 0, 1, 0]
# print(count_quadruplets_with_sum(nums, 0))  # Output: 3
