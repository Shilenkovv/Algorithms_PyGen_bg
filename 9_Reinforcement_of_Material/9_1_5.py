from collections import Counter
from math import floor, log10


def most_frequent_digit_length(nums: list[int]) -> int:
    cntr = Counter(list(map(lambda x: floor(log10(x)) + 1, nums)))

    max_cnt = -float('inf')
    for k in sorted(cntr):
        if cntr.get(k) >= max_cnt:
            max_k = k
            max_cnt = cntr.get(k)
    return max_k


# print(most_frequent_digit_length([779, 645, 579, 186, 488, 849, 471]))
