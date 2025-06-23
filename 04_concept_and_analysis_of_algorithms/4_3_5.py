from string import ascii_lowercase


def letter_by_sum(letters: list) -> str:
    """
    Computes the letter corresponding to the sum of positions of valid lowercase
    English letters in the input list. The resulting letter is determined by
    taking the sum modulo 26.

    Args:
        letters (list): A list of characters. Only lowercase English letters
                        ('a' to 'z') are considered in the computation.

    Returns:
        str: A single lowercase letter representing the result of the sum modulo 26.
    """
    tot = 0
    for c in letters:
        if c in ascii_lowercase:
            tot += ascii_lowercase.find(c) + 1
    return ascii_lowercase[(tot - 1) % 26]
