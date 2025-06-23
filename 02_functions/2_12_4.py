from math import log2


def iterated_log(n: int) -> int:
    """Calculate the number of times the logarithm base 2 can be iteratively applied
    to a number until it becomes less than or equal to 1.

    Args:
        n (int): A positive integer where 1 <= n <= 10^10000.

    Returns:
        int: The number of iterations required to reduce `n` to 1 or less
        using the base-2 logarithm.
    """
    cnt = 0
    while n > 1:
        n = log2(n)
        cnt += 1
    return cnt
