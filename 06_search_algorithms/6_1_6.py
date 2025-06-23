def find_number(nums):
    if len(nums) == 1:
        return nums[0]
    i = 0
    while i < len(nums):
        if i == len(nums) - 1:
            return nums[-1]
        if nums[i] != nums[i + 1]:
            return nums[i]
        i += 2
