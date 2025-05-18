def max_product_of_three(nums: list[int]) -> int:
    if len(nums) == 3:
        return nums[0] * nums[1] * nums[2]
    max_value_1 = max_value_2 = max_value_3 = -float('inf')
    min_value_1 = min_value_2 = float('inf')
    for num in nums:
        if num > max_value_1:
            max_value_1, max_value_2, max_value_3 = num, max_value_1, max_value_2
        elif num > max_value_2:
            max_value_2, max_value_3 = num, max_value_2
        elif num > max_value_3:
            max_value_3 = num
        if num < min_value_1 and num < 0:
            min_value_1, min_value_2 = num, min_value_1
        elif num < min_value_2 and num < 0:
            min_value_2 = num
    return (
        max(max_value_1 * max_value_2 * max_value_3, min_value_1 * min_value_2 * max_value_1)
        if min_value_1 != float('inf') and min_value_2 != float('inf')
        else max_value_1 * max_value_2 * max_value_3
    )


# assert max_product_of_three([5, 2, 6, 1, 7]) == 210
# assert max_product_of_three([1, 2, 3]) == 6
# assert max_product_of_three([-1, -2, -3]) == -6
# assert max_product_of_three([-5, -2, 4, 2, 4]) == 40
# assert max_product_of_three([-20, -2, 3, 50, 10]) == 2000
# assert max_product_of_three([-20, 1, 3, 50, 10]) == 1500
# assert third_max_value([3, 2, 1]) == 1
# assert third_max_value([-1, -2, -3]) == -3
# assert min_product_of_two([1, 1, 1, 1, 1]) == 1
# assert min_product_of_two([1, 2, 1, 3, 4]) == 1
