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


def is_hyper_prime(n: int) -> bool:
    while n != 0:
        if not is_prime(n):
            return False
        n //= 10
    return True


print(is_hyper_prime(17))  # False
print(is_hyper_prime(733))  # True
print(is_hyper_prime(43))  # False
print(is_hyper_prime(313))  # True
