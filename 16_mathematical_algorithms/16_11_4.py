def tribonacci(n: int) -> int:
    if n <= 2:
        return 1
    prev_prev, prev, cur = 1, 1, 2
    for _ in range(n - 3):
        prev_prev, prev, cur = prev, cur, prev_prev + prev + cur
    return cur


print(tribonacci(1))
print(tribonacci(3))
print(tribonacci(10))
