from collections import deque
from typing import List


def discarding_order(n: int) -> List[int]:
    deq: deque[int] = deque(range(1, n + 1))
    ans: List[int] = []

    while len(deq) > 1:
        ans.append(deq.popleft())
        deq.append(deq.popleft())

    return ans


print(discarding_order(6))  # [1, 3, 5, 2, 6]
print(discarding_order(3))  # [1, 3]
print(discarding_order(1))  # []
