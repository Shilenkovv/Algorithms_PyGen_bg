def missing_numbers(n: int, nums: list[int]) -> tuple[int, int]:
    should_be = ((1 + n) * n) // 2
    we_have = sum(nums)
    a_and_b = should_be - we_have
    should_be_sqaured = (n * (n + 1) * (2 * n + 1)) // 6
    we_have_squared = sum(map(lambda x: x**2, nums))
    a_and_b_squared = should_be_sqaured - we_have_squared

    d = 4 * a_and_b**2 - 8 * (a_and_b**2 - a_and_b_squared)
    a = int((2 * a_and_b + d**0.5) // 4)
    b = int(a_and_b - a)
    return (min(a, b), max(a, b))


# print(missing_numbers(5, [2, 5, 3]))

# print(ar_sum(6, 2))
# print(days_for_solve(25, 2))
