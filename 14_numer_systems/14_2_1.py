def count_even_digits(n: int) -> int:
    ans = 0
    while n > 0:
        if not (n % 10) % 2:
            ans += 1
        n //= 10
    return ans


# print(count_even_digits(123))  # 1
# print(count_even_digits(2468))  # 4
# print(count_even_digits(3333333))  # 0
