def min_even_digit(num: int) -> int:
    cur_min_even = float('inf')
    for c in str(num):
        cur_digit = int(c)
        if not cur_digit % 2:
            cur_min_even = min(cur_min_even, cur_digit)
    if cur_min_even == float('inf'):
        return -1
    return cur_min_even
