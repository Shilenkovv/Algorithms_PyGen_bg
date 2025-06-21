def has_triplet_sum(nums: list[int]) -> bool:
    n = len(nums)
    nums.sort()

    for i in range(n - 1, -1, -1):
        left = 0
        right = i - 1
        while left < right:
            if nums[i] == nums[left] + nums[right]:
                return True
            elif nums[i] > nums[left] + nums[right]:
                left += 1
            else:
                right -= 1

    return False
