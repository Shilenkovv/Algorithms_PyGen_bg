from collections import deque
from typing import List, Tuple


def operation_result(nums: List[int], k: int) -> Tuple[int, int]:
    deq: deque[int] = deque(nums)
    for _ in range(k - 1):
        a, b = deq.popleft(), deq.popleft()
        if a <= b:
            a, b = b, a
        deq.appendleft(a)
        deq.append(b)

    return (deq.popleft(), deq.popleft())


print(operation_result([1, 2, 3, 4, 5], 1))  # (1, 2)
print(operation_result([1, 2, 3, 4, 5], 9))  # (5, 1)
print(operation_result([4, -1], 2))  # (4, -1)
