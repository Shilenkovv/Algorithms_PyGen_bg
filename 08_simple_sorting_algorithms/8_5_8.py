from collections import Counter


def advanced_sort(nums: list[int]) -> list[list[int]]:
    counter_nums = Counter(nums)

    final_list = []
    for k in counter_nums:
        final_list.append([k] * counter_nums.get(k))
    return final_list


# print(advanced_sort([2, 4, 4, 2]))
