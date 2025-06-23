def move_min_elements(nums):
    # Find the minimum value in the list
    min_value = min(nums)

    # Separate the elements into two groups: min_value elements and others
    min_elements = [num for num in nums if num == min_value]
    other_elements = [num for num in nums if num != min_value]

    # Combine the groups: min_value elements first, then other elements
    nums[:] = min_elements + other_elements


# data = [1, 4, 1, 3, 1, 2]
# move_min_elements(data)
# print(data)
