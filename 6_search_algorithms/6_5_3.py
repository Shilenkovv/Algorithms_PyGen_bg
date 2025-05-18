def find_silver_score(nums: list[int]) -> int:
    first_max = second_max = third_max = -float('inf')
    for num in nums:
        if num > first_max:
            first_max, second_max, third_max = num, first_max, second_max
        elif num > second_max and num != first_max:
            second_max, third_max = num, second_max
        elif num > third_max and num != second_max and num != first_max:
            third_max = num
    return second_max


# assert find_silver_score([40, 20, 30, 10, 20]) == 30
# assert find_silver_score([5, 2, 5, 3, 3, 1]) == 3
# assert find_silver_score([10, 10, 5, 5]) == 5
# assert find_silver_score([1, 1, 3, 2, 2]) == 2
# assert third_max_value([3, 2, 1]) == 1
# assert third_max_value([-1, -2, -3]) == -3
# assert min_product_of_two([1, 1, 1, 1, 1]) == 1
# assert min_product_of_two([1, 2, 1, 3, 4]) == 1
