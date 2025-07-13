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


def first_primes_sum_divisible_by(k: int) -> int:
    if k <= 2:
        return 1
    cnt = 1
    tot = 2
    cur_num = 3
    while tot % k:
        while not is_prime(cur_num):
            cur_num += 1
        tot += cur_num
        cnt += 1
        cur_num += 1
    return cnt


print(first_primes_sum_divisible_by(1))  # 2 ⋮ 1
print(first_primes_sum_divisible_by(7))  # 2 + 3 + 5 + 7 + 11 = 28 ⋮ 7
