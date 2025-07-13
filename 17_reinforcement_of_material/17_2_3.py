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


def max_left_bound(b: int, k: int) -> int:
    cur_cnt = 1 if is_prime(b) else 0
    while cur_cnt != k:
        b -= 1
        while not is_prime(b):
            b -= 1
        cur_cnt += 1
    return b


print(max_left_bound(10, 3))
