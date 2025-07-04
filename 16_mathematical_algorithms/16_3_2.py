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


def twin_prime(num: int) -> int:
    if not is_prime(num):
        return -1
    if is_prime(num - 2):
        return num - 2
    if is_prime(num + 2):
        return num + 2
    return -1


# print(twin_prime(11))
# print(twin_prime(10))
# print(twin_prime(5))
# print(twin_prime(6))
# print(twin_prime(2))
