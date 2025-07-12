def count_trailing_zeroes_in_factorial(n: int) -> int:
    cur_zeros = 0
    divisor = 5
    while divisor <= n:
        cur_zeros += n // divisor
        divisor *= 5
    return cur_zeros


# print(count_trailing_zeroes_in_factorial(4))  # 0
# print(count_trailing_zeroes_in_factorial(5))  # 1
# print(count_trailing_zeroes_in_factorial(10))  # 10! = 3628800 # 2
# print(count_trailing_zeroes_in_factorial(15))  # 15! = 1307674368000 # 3
