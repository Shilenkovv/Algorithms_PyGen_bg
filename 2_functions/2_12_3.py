from math import ceil, log2


def closest_exponent(n: int) -> int:
    """Find the smallest power of 2 that is greater than or equal to the given number.

    Args:
        n (int): A positive integer where 1 <= n <= 10^1000.

    Returns:
        int: The exponent `k` such that 2^k is greater than or equal to `n`.
    """
    return ceil(log2(n))
