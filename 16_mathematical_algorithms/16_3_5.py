def count_factors(num: int) -> int:
    count = 0
    divisor = 2
    while divisor * divisor <= num:
        while num % divisor == 0:
            count += 1
            num //= divisor
        divisor += 1
    if num > 1:
        count += 1
    return count


# print(count_factors(2))  # 1
# print(count_factors(10))  # 2
# print(count_factors(32))  # 5
# print(count_factors(49))  # 2
# print(count_factors(100))  # 4
