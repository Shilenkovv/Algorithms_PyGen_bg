from collections import deque
from typing import List


def bin_sequence(n: int) -> List[str]:
    result = []
    q = deque()
    q.append('1')
    for _ in range(n):
        curr = q.popleft()
        result.append(curr)
        q.append(curr + '0')
        q.append(curr + '1')
    return result
