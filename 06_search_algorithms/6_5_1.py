def min_product_of_two(nums: list[int]) -> int:
    min_value_1 = min_value_2 = float('inf')
    for elem in nums:
        if elem < min_value_1:
            min_value_2 = min_value_1
            min_value_1 = elem
        elif elem < min_value_2:
            min_value_2 = elem
    return min_value_1 * min_value_2


# assert min_product_of_two([5, 2, 6, 1, 7]) == 2
# assert min_product_of_two([1, 1, 1, 1, 1]) == 1
# assert min_product_of_two([1, 2, 1, 3, 4]) == 1
