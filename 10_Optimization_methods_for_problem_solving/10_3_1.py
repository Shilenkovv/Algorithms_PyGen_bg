def count_pairs_with_sum(nums: list[int], k: int) -> int:
    left, right = 0, len(nums) - 1
    counter = 0
    while left < right:
        cur_sum = nums[left] + nums[right]
        if cur_sum == k:
            counter += 1
            left += 1
            right -= 1
        elif cur_sum < k:
            left += 1
        elif cur_sum > k:
            right -= 1
    return counter


# print(count_pairs_with_sum([1, 1, 2, 2, 3], 4))  # пары: (1, 3), (2, 2) # 2
