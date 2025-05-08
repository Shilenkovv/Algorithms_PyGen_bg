def hamming_distance(s1: str, s2: str) -> int:
    """Calculate the Hamming distance between two strings of equal length.

    Args:
        s1 (str): Given string, where 1 <= len(s1) <= 10^3.
        s2 (str): Second string, where len(s2) == len(s1).

    Returns:
        int: The Hamming distance between the two strings.
    """
    ans = 0
    for i in range(len(s1)):
        ans += s1[i] != s2[i]
    return ans
