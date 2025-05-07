def drop_one_and_five(n: int) -> int:
    """
    Removes all digits 1 and 5 from the given number.
    If the resulting number is empty, returns 0.

    Args:
        n (int): An integer (0 ≤ n ≤ 10^9).

    Returns:
        int: The number without digits 1 and 5, or 0 if no digits remain.
    """
    result = 0
    multiplier = 1

    while n > 0:
        digit = n % 10
        if digit != 1 and digit != 5:
            result += digit * multiplier
            multiplier *= 10
        n //= 10

    return result
