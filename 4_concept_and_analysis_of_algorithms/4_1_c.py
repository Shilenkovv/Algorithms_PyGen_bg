def max_guests(n: int, m: int) -> int:
    """Calculate the maximum number of guests.

    Args:
        n (int): Number of floors, rooms lokated on each floor, except the first one. 1 <= n <= 10^3.
        m (int): Number of rooms on the each floor(except the first one). 1 <= m <=10^3.

    Returns:
        int: Maximum number of guests what can be accommodated.
    """
    return (n - 1) * m * 3
