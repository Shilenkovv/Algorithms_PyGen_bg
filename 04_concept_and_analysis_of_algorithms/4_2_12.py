from math import log10


def make_palindrome(n: int) -> int:
    """
    Attempts to transform the given integer into a palindrome by reversing and
    adding its digits iteratively. If a palindrome is not formed within 6 iterations,
    the function returns -1.

    Args:
        n (int): The integer to be transformed into a palindrome, where 1 <= n <= 10^6.

    Returns:
        int: The resulting palindrome if successful within 6 iterations; otherwise -1.
    """
    if n == 1:
        return 1
    power = 10
    n_len = int(log10(n)) + 1
    for _ in range(6):
        rev_num = 0
        n_len = int(log10(n)) + 1
        is_palindrome = True
        for i in range(n_len // 2):
            a = (n % (power ** (n_len - i))) // (power ** (n_len - i - 1))
            b = (n % (power ** (i + 1))) // (power**i)
            rev_num += b * power ** (n_len - i - 1) + a * power**i
            if a != b:
                is_palindrome = False
        if is_palindrome:
            return n
        elif n_len % 2 == 1:
            i += 1
            rev_num += (n % (power ** (i + 1))) // (power**i) * power**i
        n += rev_num
    return -1
