def sum_of_seven_smallest(nums: list[int]) -> int:
    n = len(nums)
    tot_sum = 0

    for i in range(7):
        index_min = i

        for j in range(i + 1, n):
            if nums[j] < nums[index_min]:
                index_min = j

        if i != index_min:
            nums[i], nums[index_min] = nums[index_min], nums[i]
        tot_sum += nums[i]
    return tot_sum


# print(sum_of_seven_smallest([2, 7, 3, 6, 10, 4, 1, 9, 5, 8]))

# data = [0, 6, -5, 6, 7]
# selection_sort(data)
# print(data)
