def third_max_value(nums: list[int]) -> int:
    first_max = second_max = third_max = -float('inf')
    for num in nums:
        if num > first_max:
            first_max, second_max, third_max = num, first_max, second_max
        elif num > second_max:
            second_max, third_max = num, second_max
        elif num > third_max:
            third_max = num
    return third_max


# assert third_max_value([4, 8, 6, 10]) == 6
# assert third_max_value([4, 4, 4, 4]) == 4
# assert third_max_value([1, 2, 3]) == 1
# assert third_max_value([3, 2, 1]) == 1
# assert third_max_value([-1, -2, -3]) == -3
# assert min_product_of_two([1, 1, 1, 1, 1]) == 1
# assert min_product_of_two([1, 2, 1, 3, 4]) == 1
