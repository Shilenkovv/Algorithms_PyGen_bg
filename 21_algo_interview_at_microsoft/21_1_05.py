from typing import List


def count_sublists_with_lower_product(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0

    product = 1
    count = 0
    left = 0

    for right in range(len(nums)):
        product *= nums[right]

        while product >= k and left <= right:
            product //= nums[left]
            left += 1

        count += right - left + 1

    return count


# print(count_sublists_with_lower_product([5, 2, 4, 3], 25))  # 8
# print(count_sublists_with_lower_product([5, 2, 4, 3], 1))  # 0
# print(count_sublists_with_lower_product([1], 1))  # 0
# print(count_sublists_with_lower_product([2, 7, 1, 5], 2))  # 1
# print(count_sublists_with_lower_product([5, 5, 5, 5], 26))  # 7
# print(count_sublists_with_lower_product([1, 2, 3, 4], 0))  # 0
