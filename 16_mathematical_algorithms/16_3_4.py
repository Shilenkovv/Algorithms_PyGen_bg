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


def count_primes_ending_with(k: int) -> int:
    ans = 0
    for i in range(1000, 10000):
        if i % 10 == k:
            if is_prime(i):
                ans += 1
        else:
            continue

    return ans


# print(count_primes_ending_with(3))
