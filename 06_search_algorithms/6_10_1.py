from math import floor, sqrt


def jump_search(nums: list[int], target: int) -> int:
    n = len(nums)

    if n == 0:
        return -1

    block_size = floor(sqrt(n))
    left, right = 0, block_size - 1

    while nums[right] > target:
        left = right + 1
        right = min(right + block_size, n - 1)

        if left >= n:
            return -1

    for i in range(left, right + 1):
        if nums[i] == target:
            return i

    return -1
