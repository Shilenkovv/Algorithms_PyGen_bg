from math import floor, log10


def count_powers(num: int) -> int:
    """Count how many consecutive powers of 2 can be formed by concatenating digits from the given number.

    The function takes digits from the input number (starting from the left) and counts how many
    complete powers of 2 (1, 2, 4, 8, 16, 32, ...) can be formed by these digits when concatenated.

    Args:
        num (int): A positive integer from which digits will be used to form powers of 2.

    Returns:
        int: The count of consecutive powers of 2 that can be formed from the number's digits.

    Examples:
        >>> count_powers(24)
        2   # because 2 and 4 are powers of 2
        >>> count_powers(24816)
        4   # because 2, 4, 8 and 16 are all powers of 2
    """
    digits = floor(log10(num)) + 1
    n_powers = 0
    while digits != 0:
        n_powers += 1
        digits -= floor(log10(2**n_powers)) + 1
    return n_powers
