def has_nine_divisors(number):
    count = 1
    for n in range(1, number // 2 + 1):
        if number % n == 0:
            count += 1
    return count == 9


def nine_divisors(n):
    count = 0
    for num in range(1, n + 1):
        if has_nine_divisors(num):
            count += 1
    return count
