def count_numbers(n, k):
    ans = 0
    for i in range(1, n + 1):
        if i - sum([int(c) for c in str(i)]) >= k:
            ans += 1
    return ans
