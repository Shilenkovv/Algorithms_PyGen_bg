def time_zone(h: int, a: int, b: int) -> int:
    """Returns the time in a different time zone.

    Args:
        h (int): Time in hours for Timur, where 0 <= h <= 23.
        a (int): Time zone of Timur, where -11 <= a <= 12.
        b (int): Time zone of Arthur, where -11 <= b <= 12.

    Returns:
        int: Time in hours for Arthur, where 0 <= result <= 23.
    """
    return (h - a + b) % 24
