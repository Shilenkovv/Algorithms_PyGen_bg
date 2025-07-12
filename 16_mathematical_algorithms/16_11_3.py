def is_fibonacci(n: int) -> bool:
    prev, cur = 1, 1
    while cur <= n:
        if n == cur:
            return True
        prev, cur = cur, prev + cur
    return False
