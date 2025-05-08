def count_days(cur: int) -> int:
    """
    Calculates the number of days that have passed since the cactus was purchased,
    given its current height. The cactus starts at height 2 cm and grows according
    to the formula: height = 2 * height + 1 per day.

    Args:
        cur (int): The current height of the cactus (2 ≤ cur ≤ 10^10).

    Returns:
        int: The number of days that have passed since the cactus was purchased.
    """
    # if cur % 2 == 0:
    #     return 0
    days = 0
    while cur % 2:
        cur = (cur - 1) / 2
        days += 1
    return days
