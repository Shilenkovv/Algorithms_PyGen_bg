from typing import List


def min_steps_to_replace_zeros(bin_list: List[int]) -> int:
    if sum(bin_list) == 0:
        return -1
    elif sum(bin_list) == len(bin_list):
        return 0

    steps = 0
    cur_zeros = 0

    one_found = False
    for elem in bin_list:
        if elem == 0:
            cur_zeros += 1
        elif elem == 1:
            if cur_zeros != 0:
                if one_found:
                    steps = max(cur_zeros // 2 + cur_zeros % 2, steps)
                else:
                    steps = max(steps, cur_zeros)
                cur_zeros = 0
            one_found = True
    if cur_zeros != 0:
        steps = max(steps, cur_zeros)
    return steps


# print(min_steps_to_replace_zeros([1, 0, 1, 0]))  # 1
# print(min_steps_to_replace_zeros([0, 0, 1, 0, 0]))  # 2
# print(min_steps_to_replace_zeros([0, 0, 0, 0, 0]))  # -1
# print(min_steps_to_replace_zeros([1, 1, 1, 1]))  # 0
# print(min_steps_to_replace_zeros([0]))  # -1
# print(min_steps_to_replace_zeros([0, 0, 0, 0, 0, 1]))  # 5
# print(min_steps_to_replace_zeros([1, 0, 0, 1, 1, 1, 0]))  # 1
# print(min_steps_to_replace_zeros([0, 0, 0, 1, 0, 1, 1, 0, 0, 0]))  # 3
# print(min_steps_to_replace_zeros([0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]))  # 2
# print(min_steps_to_replace_zeros([0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1]))  # 1
