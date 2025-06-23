def has_intersecting_segments(nums: list[tuple[int, int]]) -> bool:
    new_nums = sorted(nums)
    for i in range(1, len(new_nums)):
        if new_nums[i][0] <= new_nums[i - 1][1]:
            return True
    return False


# print(has_intersecting_segments([(2, 3), (4, 6), (7, 10)]))  # False
# print(has_intersecting_segments([(2, 3), (3, 5)]))  # True
# print(has_intersecting_segments([(3, 6), (1, 7)]))  # True
# print(has_intersecting_segments([(2, 4), (3, 5)]))  # True
# print(has_intersecting_segments([(0, 7), (-1, 6)]))  # True
# print(has_intersecting_segments([(-7, -6), (-2, 2)]))  # False
