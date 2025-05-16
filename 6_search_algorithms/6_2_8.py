def drop_digit(digits: str) -> int:
    """
    Removes one digit from the given number string to maximize the resulting integer.

    Args:
        digits (str): A string of digits representing a number, where
                      2 <= len(digits) <= 10^5 and each character in the string is a digit (0-9).

    Returns:
        int: The maximum possible integer obtained by removing one digit from the input string.
    """
    for i in range(1, len(digits)):
        if digits[i] > digits[i - 1]:
            return digits[: i - 1] + digits[i:]
    return digits[:-1]
