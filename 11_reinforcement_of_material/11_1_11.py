from collections import Counter
from typing import List


def all_permutations(s1: str, s2: str) -> List[int]:
    left, right = 0, len(s2)
    s2_c = Counter(s2)
    s1_c = Counter(s1[left:right])
    ans = []

    while right < len(s1):
        if s1_c == s2_c:
            ans.append(left)
        left += 1
        right += 1
        if s1[right - 1] not in s1_c:
            s1_c[s1[right - 1]] = 1
        else:
            s1_c[s1[right - 1]] += 1
        s1_c[s1[left - 1]] -= 1
        if s1_c[s1[left - 1]] == 0:
            s1_c.pop(s1[left - 1])
    if s1_c == s2_c:
        ans.append(left)
    return ans


print(all_permutations('baba', 'ba'))
print(all_permutations('baceabcd', 'abc'))  # [0, 4]
