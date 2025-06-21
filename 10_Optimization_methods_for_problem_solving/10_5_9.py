def count_sublists_with_sum(binary_list: list[int], k: int) -> int:
    counter = 0
    current_sum = 0
    sum_freq = {}

    for num in binary_list:
        current_sum += num
        if current_sum == k:
            counter += 1

        if current_sum - k in sum_freq:
            counter += sum_freq[current_sum - k]
        sum_freq[current_sum] = sum_freq.get(current_sum, 0) + 1

    return counter


# print(count_sublists_with_sum([1, 1, 0, 1], 2))  # [1, 1], [1, 1, 0], [1, 0, 1] # 3
# print(count_sublists_with_sum([0, 0, 0], 0))  # [0], [0], [0], [0, 0], [0, 0], [0, 0, 0]
# print(longest_sublist_of_ones([1, 1, 1, 0, 1, 1, 0, 1]))  # 5
# print(longest_sublist_of_ones([0, 0, 0, 0, 0]))  # 0
# print(longest_sublist_of_ones([1]))  # 0
# print(longest_sublist_of_ones([1, 1, 0, 0, 1]))  # 2
