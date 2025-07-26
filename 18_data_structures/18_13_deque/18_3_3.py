from collections import deque
from typing import List


def slice(dq: deque[int], start: int, end: int) -> List[int]:
    ans: List[int] = []
    for _ in range(start):
        dq.rotate(-1)
    for _ in range(end - start):
        ans.append(dq.popleft())
    return ans


print(slice(deque([1, 2, 3, 4, 5]), 1, 3))
