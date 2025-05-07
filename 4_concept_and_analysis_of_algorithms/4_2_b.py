def mystery(n: int) -> int:
    """Calculate the next even number after n.

    Args:
        n (int): Given number, where 0 <= n <= 10^3.

    Returns:
        int: The next even number after n.
    """
    n += 1
    while n % 2 != 0:
        n += 1
    return n
