from math import gcd
from typing import List


def all_fractions(n: int) -> List[str]:
    ans = dict()
    for i in range(2, n + 1):
        for j in range(1, i):
            if gcd(i, j) == 1:
                ans[j / i] = str(j) + '/' + str(i)
    ans_list: List[str] = []
    for k in sorted(ans):
        ans_list.append(ans.get(k))
    return ans_list


# print(all_fractions(5))
