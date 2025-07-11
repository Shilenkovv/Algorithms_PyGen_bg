from typing import List


def count_geometric_sublists(nums: List[int | float]) -> int:
    sublists_count = 0
    result = 0

    for i in range(1, len(nums) - 1):
        if nums[i] ** 2 == nums[i - 1] * nums[i + 1]:
            sublists_count += 1

        else:
            sublists_count = 0
        result += sublists_count

    return result


# print(count_geometric_sublists([-3, -3, -3, 3, 3, 3]))
# print(count_geometric_sublists([1, 2, 4, 8]))  # 3
# print(count_geometric_sublists([1, 2, 3, 4, 5]))  # 0
# print(count_geometric_sublists([1, 1, 1]))  # 1
# print(count_geometric_sublists([0.25, 0.5, 1, 2, 4]))  # 6
