from collections import Counter


def find_difference(s1: str, s2: str) -> str:
    c1 = Counter(s1)
    c2 = Counter(s2)

    for k in c2:
        if k not in c1 or c2.get(k) > c1.get(k):
            return k


# print(find_difference('geek', 'geeka'))
