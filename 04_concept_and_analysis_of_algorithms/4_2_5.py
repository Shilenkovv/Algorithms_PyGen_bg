def sum_of_squares(n: int) -> int:
    """Calculate the sum of squares of the first n natural numbers.

    Args:
        n (int): Given integer n, where 1 <= n <= 10^3

    Returns:
        int: Sum of squares of the first n natural numbers.
    Example:
        >>> sum_of_squares(3)
        14
        >>> sum_of_squares(4)
        30
    """
    return sum(i**2 for i in range(1, n + 1))
