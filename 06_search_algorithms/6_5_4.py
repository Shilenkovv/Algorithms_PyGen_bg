def max_product_of_two(nums: list[int]) -> int:
    max_value_1 = max_value_2 = -float('inf')
    min_value_1 = min_value_2 = float('inf')
    for num in nums:
        if num > max_value_1:
            max_value_1, max_value_2 = num, max_value_1
        elif num > max_value_2:
            max_value_2 = num
        if num < min_value_1:
            min_value_1, min_value_2 = num, min_value_1
        elif num < min_value_2:
            min_value_2 = num
    return max(max_value_1 * max_value_2, min_value_1 * min_value_2)


# assert find_silver_score([40, 20, 30, 10, 20]) == 30
# assert find_silver_score([5, 2, 5, 3, 3, 1]) == 3
# assert find_silver_score([10, 10, 5, 5]) == 5
# assert find_silver_score([1, 1, 3, 2, 2]) == 2
# assert third_max_value([3, 2, 1]) == 1
# assert third_max_value([-1, -2, -3]) == -3
# assert min_product_of_two([1, 1, 1, 1, 1]) == 1
# assert min_product_of_two([1, 2, 1, 3, 4]) == 1
