def longest_sublist_of_ones(nums: list[int]) -> int:
    if sum(nums) >= len(nums) - 1:
        return len(nums) - 1

    prev_len, max_len = 0, 0
    ones_counter = 0
    zero_found = False

    for i in range(len(nums)):
        if nums[i] == 1:
            ones_counter += 1
            zero_found = False
        else:
            if zero_found:
                max_len = max(max_len, prev_len)
                prev_len = 0
            else:
                zero_found = True
                if prev_len:
                    max_len = max(max_len, ones_counter + prev_len)
                prev_len = ones_counter
            ones_counter = 0

    return max(max_len, prev_len + ones_counter)


# print(longest_sublist_of_ones([1, 0, 1, 1, 1]))  # 4
# print(longest_sublist_of_ones([1, 1, 1, 1]))  # 3
# print(longest_sublist_of_ones([1, 1, 1, 0, 1, 1, 0, 1]))  # 5
# print(longest_sublist_of_ones([0, 0, 0, 0, 0]))  # 0
# print(longest_sublist_of_ones([1]))  # 0
# print(longest_sublist_of_ones([1, 1, 0, 0, 1]))  # 2
