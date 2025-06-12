from collections import defaultdict


def count_triplets_with_sum(nums1: list[int], nums2: list[int], nums3: list[int], k: int) -> int:
    a_b_sum = defaultdict(int)
    k_sub_c = defaultdict(int)
    for a in nums1:
        for b in nums2:
            a_b_sum[a + b] += 1
    for c in nums3:
        k_sub_c[k - c] += 1

    counter = 0
    for k in a_b_sum:
        counter += a_b_sum[k] * k_sub_c[k]

    return counter


# print(count_triplets_with_sum([1, 2], [0, 1], [3, 4], 5))  # (1, 1, 3), (1, 0, 4), (2, 0, 3) # 3
# print(count_triplets_with_sum([1], [1], [1], 3))  # (1, 1, 1) # 1
# print(count_triplets_with_sum([1, 1, 1], [1, 1, 1], [1, 1, 1], 1))  # 0
