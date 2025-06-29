from typing import List


def binary_shift_game_result(num: int) -> int:
    num_base_2_list: List[str] = []

    while num != 0:
        last_digit = num % 2
        num_base_2_list.append(str(last_digit))
        num //= 2
    num_base_2_list = list(reversed(num_base_2_list))

    max_base_10 = -float('inf')
    n = len(num_base_2_list)
    for i in range(n):
        new_num_base_10: int = 0
        str_num: str = ''.join(num_base_2_list[n - i : n]) + ''.join(num_base_2_list[0 : n - i])
        if str_num[0] == '0':
            continue
        for j in range(n - 1, -1, -1):
            new_num_base_10 += int(str_num[j]) * 2 ** (n - 1 - j)
        max_base_10 = max(max_base_10, new_num_base_10)

    return max_base_10


# print(binary_shift_game_result(19))  # 28
# print(binary_shift_game_result(754))  # 970
