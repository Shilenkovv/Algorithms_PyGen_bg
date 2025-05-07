def divisible(n: int) -> int:
    """Count the number of digits in n that are divisors of n.

    Args:
        n (int): Given number to check divisibility, where 1 <= n <= 10^6.

    Returns:
        int: The count of digits in n that are divisors of n.
    """
    power = 1
    ans = 0
    while power <= n:
        power *= 10
        cur_digit = (n % power) // (power / 10)
        if cur_digit != 0 and n % cur_digit == 0:
            ans += 1
    return ans
