def ar_sum(n: int, a: int, d: int = 1) -> int:
    return ((2 * a + d * (n - 1)) * n) // 2


def days_for_solve(n: int, k: int) -> int:
    left = 1
    right = 10**10
    while left <= right:
        mid = left + (right - left) // 2
        if ar_sum(mid, k) < n:
            left = mid + 1
        else:
            right = mid - 1
    return left
