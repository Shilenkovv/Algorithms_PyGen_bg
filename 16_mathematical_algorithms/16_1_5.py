from typing import List


def change_one_digit(list_num: List[int]) -> List[int]:
    cur_tot = sum(list_num)
    diff_add = 3 - cur_tot % 3
    diff_sub = cur_tot % 3 if cur_tot % 3 else 3
    for i in range(len(list_num)):
        if list_num[i] + diff_add <= 9:
            while list_num[i] + diff_add <= 9:
                list_num[i] += diff_add
                diff_add = 3
            return list_num
    for i in range(len(list_num) - 1, -1, -1):
        if list_num[i] - diff_sub >= 0:
            list_num[i] -= diff_sub
            return list_num


# print(change_one_digit([3, 5, 6]))  # [7, 5, 6]
# print(change_one_digit([1, 2, 3]))  # [7, 2, 3]
# print(change_one_digit([0]))  # [9]
# print(change_one_digit([3, 3, 3]))  # [9, 3, 3]
# print(change_one_digit([9, 9, 9]))  # [9, 9, 6]
# print(change_one_digit([9, 9, 8, 8]))
