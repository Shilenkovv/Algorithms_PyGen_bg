def swap_digits(n: int):
    """Swaps the digits of a three-digit number.

    Args:
        n (int): A three-digit integer whose digits will be swapped.

    Returns:
        int: The integer formed by swapping the digits of the input.
    """
    first = n // 100
    second = n % 100 // 10
    third = n % 10
    # Reconstruct the number with the digits swapped: third becomes the hundreds place,
    # second becomes the tens place, and first becomes the ones place.
    return third * 100 + second * 10 + first
