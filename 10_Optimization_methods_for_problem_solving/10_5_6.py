from collections import defaultdict


def contains_permutation(s1: str, s2: str) -> bool:
    left = 0
    right = len(s2)

    s1_counter = defaultdict(int)
    s2_counter = defaultdict(int)

    for i in range(right):
        s1_counter[s1[i]] += 1
        s2_counter[s2[i]] += 1

    if s1_counter == s2_counter:
        return True
    while right < len(s1):
        left += 1
        right += 1
        s1_counter[s1[left - 1]] -= 1
        s1_counter[s1[right - 1]] += 1
        if s1_counter[s1[left - 1]] == 0:
            s1_counter.pop(s1[left - 1])
        if s1_counter == s2_counter:
            return True

    return False


# print(contains_permutation('stepik', 'pet'))  # True
# print(contains_permutation('python', 'py'))  # True
# print(contains_permutation('geek', 'geek'))  # True
# print(contains_permutation('beegeek', 'bgk'))  # False
