from collections import deque


def delete(dq: deque[int], index: int) -> None:
    for _ in range(index):
        dq.rotate(-1)
    dq.popleft()
    for _ in range(index):
        dq.rotate()


dq = deque([1, 2, 3, 4, 5])
delete(dq, 2)
print(*dq)
