from collections import defaultdict


def count_valid_quadruplets(
    nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]
) -> int:
    left_part = defaultdict(int)
    right_part1 = defaultdict(int)
    right_part2 = defaultdict(int)

    for a in nums1:
        for b in nums2:
            left_part[a + b] += 1

    for c in nums3:
        for d in nums4:
            right_part1[3 * d - c] += 1
            if d != 0:
                right_part2[d - c] += 1

    counter = 0
    for k in left_part:
        counter += left_part[k] * right_part1[k]
        counter += left_part[k] * right_part2[k]

    return counter


# print(count_valid_quadruplets([1, 2], [3, 4], [3, 6], [7, 8]))  # 3
# print(count_valid_quadruplets([2, -1, 3], [-1, 0, 1], [4, 2, 5], [-2, 0]))  # 1
