def sum_of_digits_in_base(num: int, base: int) -> int:
    ans = 0

    while num != 0:
        ans += num % base
        num //= base
    return ans


print(sum_of_digits_in_base(14, 2))  # 3
print(sum_of_digits_in_base(44, 3))  # 6
print(sum_of_digits_in_base(442, 16))  # 22
