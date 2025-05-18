def min_difference(num: int) -> int:
    a = 1
    b = 0
    min_diff = float('inf')
    for i in range(2, num // 2 + num % 2):
        if not num % i:
            b = i
            min_diff = min(min_diff, b - a)
            if min_diff == 1:
                return min_diff
            a, b = b, 0
    return min(min_diff, num - a)


# # assert min_difference(18) == 1
# assert min_difference(2) == 1
# assert min_difference(25) == 4
