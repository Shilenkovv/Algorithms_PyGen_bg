def min_product_of_three(nums: list[int]) -> int:
    if len(nums) <= 3:
        return nums[0] * nums[1] * nums[2]
    sorted_nums = sorted(nums)
    first_min = second_min = third_min = float('inf')
    for elem in nums:
        if elem <= first_min:
            first_min, second_min, third_min = elem, first_min, second_min
        elif elem <= second_min:
            second_min, third_min = elem, second_min
        elif elem <= third_min:
            third_min = elem
    return min(
        first_min * second_min * third_min, sorted_nums[0] * sorted_nums[-1] * sorted_nums[-2]
    )


# print(min_product_of_three([0, 1, 2, 3]))
# print(min_product_of_three([5, 2, 6, 1, 7]))
# print(min_product_of_three([1, 2, 3]))
