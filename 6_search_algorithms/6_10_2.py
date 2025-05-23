from math import floor, sqrt


def jump_search(nums: list[int], target: int) -> int:
    n = len(nums)

    if n == 0:
        return -1

    block_size = floor(sqrt(n))
    left, right = 0, block_size - 1

    while right + 1 != n and (nums[right] < target or nums[right + 1] == target):
        left = right + 1
        right = min(right + block_size, n - 1)

        if left >= n:
            return -1

    for i in range(right, left - 1, -1):
        if nums[i] == target:
            return i

    return -1


# print(jump_search([1, 3, 5, 7, 9], 5))  # 2
# print(jump_search([1, 1, 1, 3, 5, 5, 5, 7, 9, 9, 9], 5))  # 6
# print(jump_search([1, 1, 1, 3, 5, 5, 5, 7, 9, 9, 9], 10))  # -1
