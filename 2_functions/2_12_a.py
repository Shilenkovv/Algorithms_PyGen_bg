from math import floor, log10


def count_digits(n: int) -> int:
    """Calculate the number of digits in a given integer.

    Args:
        n (int): A positive integer where 1 <= n <= 10^5000.

    Returns:
        int: The number of digits in the integer `n`.
    """
    return floor(log10(n)) + 1
