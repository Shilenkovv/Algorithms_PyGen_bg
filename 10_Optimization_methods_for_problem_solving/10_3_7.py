def alternate_order(nums: list[int]) -> tuple[int, int]:
    left, right = 0, len(nums) - 1
    ans = []
    while left < right:
        ans.append(nums[left])
        ans.append(nums[right])
        left += 1
        right -= 1
    if left == right:
        ans.append(nums[left])

    return ans


# print(alternate_order([1]))  # [1]
# # print(alternate_order([1, 2, 3, 4, 5, 6])) # [1, 6, 2, 5, 3, 4]
# print(alternate_order([1, 3, 5, 4, 2]))  # [1, 2, 3, 4, 5]
