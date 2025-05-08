def longest_substring_without_vowels(s: str) -> int:
    """Calculate the length of the longest substring without vowels.

    Args:
        s (str): Given string, which may contain vowels. 1 <= len(s) <= 10^3.

    Returns:
        int: Length of the longest substring without vowels.
        If there are no consonants, return 0.
        If the string is empty, return 0.
    """
    cur_len = 0
    max_len = 0
    vowels = set('aeiouAEIOU')
    for char in s:
        if char not in vowels:
            cur_len += 1
            max_len = max(max_len, cur_len)
        else:
            cur_len = 0
    return max_len
