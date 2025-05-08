def mystery(n: int) -> int:
    """Calculcates the number of circles in a number.

    Args:
        n (int): Given number, 0 <= n <= 10^4.

    Returns:
        int: Number of circles in the number.
    """
    ans = 0
    num = str(n)
    for elem in num:
        if elem in ['0', '6', '9']:
            ans += 1
        elif elem == '8':
            ans += 2
    return ans
