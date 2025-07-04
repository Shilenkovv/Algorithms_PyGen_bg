def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def digits_sum(n: int) -> int:
    ans = 0
    while n != 0:
        ans += n % 10
        n //= 10
    return ans


def prime_with_max_digit_sum(a: int, b: int) -> int:
    ans = -1
    max_dig_sum = -1
    for i in range(a, b + 1):
        if is_prime(i):
            cur_dig_sum = digits_sum(i)
            if cur_dig_sum >= max_dig_sum:
                max_dig_sum = cur_dig_sum
                ans = i
    return ans


# print(prime_with_max_digit_sum(10, 25))  # 19
