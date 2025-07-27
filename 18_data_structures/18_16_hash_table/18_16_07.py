from collections import Counter


def can_construct(s1: str, s2: str) -> bool:
    cntr1: dict[str, int] = Counter(s1)
    cntr2: dict[str, int] = Counter(s2)

    for k in cntr2:
        if k not in cntr1 or cntr2[k] > cntr1[k]:
            return False
    return True
