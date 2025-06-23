def max_nearby_product(nums: list[int]) -> tuple[int]:
    max_mul = -float('inf')
    for i in range(1, len(nums)):
        cur_mul = nums[i] * nums[i - 1]
        max_mul = max(max_mul, cur_mul)
    return max_mul
