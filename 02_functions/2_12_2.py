from math import log2


def is_power_of_two(n: int) -> bool:
    """Check if a given integer is a power of two.

    Args:
        n (int): A positive integer where 1 <= n <= 10^1000.

    Returns:
        bool: True if the number is a power of two, otherwise False.
    """
    return log2(n).is_integer()
