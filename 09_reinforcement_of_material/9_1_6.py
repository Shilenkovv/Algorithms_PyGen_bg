def sum_of_products(nums: list[int]) -> int:
    nums.sort()
    tot_sum = 0

    for i in range(len(nums) // 2):
        tot_sum += nums[i] * nums[len(nums) - 1 - i]
    return tot_sum


# print(sum_of_products([1, 6, 4, 2, 3, 5]))
