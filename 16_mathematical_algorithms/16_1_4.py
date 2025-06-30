def is_divisible_by_thirty_three(str_num: str) -> bool:
    even_sum = 0
    odd_sum = 0

    for i in range(len(str_num)):
        if (i + 1) % 2:
            even_sum += int(str_num[i])
        else:
            odd_sum += int(str_num[i])
    if (even_sum + odd_sum) % 3:
        return False
    if (even_sum - odd_sum) % 11:
        return False
    return True


# print(is_divisible_by_thirty_three('33'))  # True
# print(is_divisible_by_thirty_three('99'))  # True
# print(is_divisible_by_thirty_three('100'))  # False
# print(is_divisible_by_thirty_three('0'))  # True
