def training_time(n: int, m: int, s: int, b: int) -> tuple[int, int]:
    """Calculate the total training time in minutes and seconds.

    Args:
        n (int): Number of training sessions, where 1 <= n <= 10^3.
        m (int): Number of minutes for each training session, where 1 <= m <= 59.
        s (int): Number of seconds for each training session, where 0 <= s <= 59.
        b (int): Number of seconds for the break between training sessions, where 0 <= b <= 120.

        It is garanteed that the total time for each training session is not zero.

    Returns:
        tuple[int, int]: Minutes and seconds of the total training time.
    """
    if n == 1:
        return (m, s)
    total_time = n * (m * 60 + s) + b * (n - 1)
    return (total_time // 60, total_time % 60)
