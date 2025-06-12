from collections import defaultdict


def count_pythagorean_triplets(nums1: list[int], nums2: list[int], nums3: list[int]) -> int:
    right = defaultdict(int)

    for c in nums3:
        right[c**2] += 1

    counter = 0

    for a in nums1:
        for b in nums2:
            tmp_left = a**2 + b**2
            if tmp_left in right:
                counter += right[tmp_left]

    return counter


# print(count_pythagorean_triplets([2, 3, 4], [4, 3], [3, 5]))  # 2
# print(count_pythagorean_triplets([-1, 0, 5], [-2, 1, 3], [4]))  # 0
# print(count_pythagorean_triplets([-3], [-4], [-5]))  # 1
