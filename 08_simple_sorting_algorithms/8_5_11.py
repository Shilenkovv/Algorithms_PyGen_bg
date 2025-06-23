def alternate_sort(nums: list[int | str]) -> list[int | str]:
    nums_dig = sorted([x for x in nums if isinstance(x, int)])
    nums_str = sorted([x for x in nums if isinstance(x, str)])
    offset = 0
    for i in range(len(nums) // 2):
        nums[offset + i] = nums_dig[i]
        nums[offset + i + 1] = nums_str[i]
        offset += 1
    return nums


# data = ['c', 'a', 2, 1, 'b', 3]
# alternate_sort(data)
# print(data)
