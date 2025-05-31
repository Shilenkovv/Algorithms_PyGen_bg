from collections import Counter


def is_subset(s1: str, s2: str) -> bool:
    s1_dict = Counter(s1)
    s2_dict = Counter(s2)

    for k in s1_dict:
        if k not in s2_dict or s1_dict.get(k) > s2_dict.get(k):
            return False
    return True


# print(is_subset('ace', 'abcd'))  # False
# print(is_subset('ace', 'aabbccddee'))  # True
# print(is_subset('aabbccddee', 'ace'))  # False
