def count_divisors(num: int) -> int:
    counter = 0
    i = 1
    while i * i <= num:
        if num % i == 0:
            if i == num // i:
                counter += 1
            else:
                counter += 2
        i += 1
    return counter


def highly_composite_num(num: int) -> bool:
    cur_divisors = count_divisors(num)
    for i in range(1, num):
        if count_divisors(i) >= cur_divisors:
            return False
    return True


# print(highly_composite_num(1))  # True
# print(highly_composite_num(12))  # True
# print(highly_composite_num(20))  # False
# print(highly_composite_num(2))  # True
# print(highly_composite_num(10**5))
