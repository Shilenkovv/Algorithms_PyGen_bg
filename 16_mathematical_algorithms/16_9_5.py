def count_lucky_nums(n: int) -> int:
    return 2 * (2**n - 1)


print(count_lucky_nums(1))  # 3, 8
print(count_lucky_nums(2))  # 3, 8, 33, 38, 83, 88
print(count_lucky_nums(3))  # 3, 8, 33, 38, 83, 88, 333, 338, 383, 388, 833, 838, 883, 888
