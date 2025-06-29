from collections import Counter


def hamming_weight(num: int) -> int:
    counter = Counter(bin(num)[2:])

    return 0 if '1' not in counter else counter['1']
