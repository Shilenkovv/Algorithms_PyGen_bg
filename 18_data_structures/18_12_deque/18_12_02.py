from collections import deque
from typing import List, Tuple


def pairwise(nums: List[int]) -> List[Tuple[int, int]]:
    deq = deque(nums)
    a, b = None, deq.popleft()
    ans: List[int] = []
    while deq:
        a, b = b, deq.popleft()
        ans.append((a, b))
    return ans


print(pairwise([1, 2, 3, 4, 5]))
