def mid_num(a: float, b: float, c: float):
    """
    Returns the middle (median) value among three given numbers.

    Args:
        a (float): The first number where -10^3 <= a <= 10^3.
        b (float): The second number where -10^3 <= b <= 10^3.
        c (float): The third number where -10^3 <= c <= 10^3.

    Returns:
        float: The middle value among the three numbers.
    """
    sorted_lst = sorted([a, b, c])
    return sorted_lst[1]
