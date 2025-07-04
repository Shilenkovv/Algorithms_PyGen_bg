from typing import Tuple


def position_in_primes_triangle(n: int) -> Tuple[int, int]:
    # Решето Эратосфена
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    i, j = 1, 1
    for idx in range(len(is_prime) - 1):
        if is_prime[idx]:
            if j == i:
                i += 1
                j = 1
            else:
                j += 1
    return (i, j)


# print(position_in_primes_triangle(2))  # (1, 1)
# print(position_in_primes_triangle(13))  # (3, 3)
