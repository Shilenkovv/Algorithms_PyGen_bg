from collections import deque
from collections.abc import Iterable
from typing import List


def last_values(iterable: Iterable[int], k: int) -> List[int]:
    deq = deque(iterable)
    for _ in range(len(deq) - k):
        deq.popleft()
    return [elem for elem in deq]


print(last_values([1, 2, 3, 4, 5], 2))
