from collections import Counter


def max_score_split(bin_s: str) -> int:
    cntr = Counter(bin_s)

    cur_zero_left = 0
    cur_one_right = 0 if '1' not in cntr else cntr['1']
    max_sum = -float('inf')
    for i in range(len(bin_s) - 1):
        if bin_s[i] == '0':
            cur_zero_left += 1
        else:
            cur_one_right -= 1
        max_sum = max(max_sum, cur_zero_left + cur_one_right)

    return max_sum


# print(max_score_split('110101'))  # 110 и 101 # 3
# print(max_score_split('10011001'))  # 100 # 11001 # 5
# print(max_score_split('01'))  # 0 и 1 # 2
# print(max_score_split('111111'))  # 1 и 11111 # 5
