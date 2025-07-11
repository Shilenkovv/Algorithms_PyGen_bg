def alternating_sum(k: int) -> int:
    neg_n = k // 2
    pos_n = neg_n + k % 2

    pos_sum = ((2 + 2 * (pos_n - 1)) * pos_n) // 2
    neg_sum = ((-2 * 2 - 2 * (neg_n - 1)) * neg_n) // 2
    return pos_sum + neg_sum


print(alternating_sum(1))  # 1
print(alternating_sum(2))  # 1 - 2 = -1
print(alternating_sum(5))  # 1 - 2 + 3 - 4 + 5 = 3
print(alternating_sum(10))  # 1 - 2 + 3 - 4 + 5 - 6 + 7 - 8 + 9 - 10 = -5
