def nearest_fibonacci(n: int) -> int:
    if n <= 3:
        return n

    prev, cur = 1, 1
    min_dist = float('inf')
    nearest_f = 1

    while prev < n:
        prev, cur = cur, prev + cur
        cur_dist = abs(n - cur)
        if cur_dist < min_dist:
            min_dist = cur_dist
            nearest_f = cur
    return nearest_f


# print(nearest_fibonacci(10))  # 8
# print(nearest_fibonacci(21))  # 21
# print(nearest_fibonacci(4))  # 3
