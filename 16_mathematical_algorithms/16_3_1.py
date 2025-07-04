def count_divisors(num: int) -> int:
    if num == 1:
        return 1
    counter = 0
    i = 1

    while i * i <= num:
        if num % i == 0:
            if i == num / i:
                counter += 1
            else:
                counter += 2
        i += 1

    return counter


# print(count_divisors(1))
# print(count_divisors(2))
# print(count_divisors(3))
# print(count_divisors(4))
# print(count_divisors(16))
