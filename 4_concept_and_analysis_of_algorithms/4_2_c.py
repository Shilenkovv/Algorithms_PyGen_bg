def mystery(n: int) -> int:
    """Calculate the sum of the first n natural numbers.

    Args:
        n (int): Given number, 1 <= n <= 10^3.

    Returns:
        int: The sum of the first n natural numbers.
    """
    return int((n**2 + n) / 2)
