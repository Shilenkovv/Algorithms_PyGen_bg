from math import log


def is_power_of_four(n: int) -> bool:
    """Check if a given integer is a power of four.

    Args:
        n (int): A positive integer where 1 <= n <= 10^1000.

    Returns:
        bool: True if the number is a power of four, otherwise False.
    """
    return log(n, 4).is_integer()
