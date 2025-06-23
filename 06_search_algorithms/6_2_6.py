def lowercase_before_uppercase(s: str) -> bool:
    """
    Checks if all lowercase letters in the string appear before any uppercase letters.

    Args:
        s (str): The input string to check, where 1 <= len(s) <= 10^5.

    Returns:
        bool: True if all lowercase letters precede uppercase letters; False otherwise.
    """
    now_upper = False
    for char in s:
        if char.islower():
            if now_upper:
                return False
        elif char.isupper():
            now_upper = True
    return True
