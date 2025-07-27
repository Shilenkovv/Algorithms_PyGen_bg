from typing import List, Set


def count_unique(words: List[str]) -> int:
    morz_dict = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
    }

    seen: Set[str] = set()

    for word in words:
        cur_morz = ''
        for cyl in word:
            cur_morz += morz_dict[cyl]
        seen.add(cur_morz)
    return len(seen)
