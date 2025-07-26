from collections import deque


def remove_all(dq: deque[int], value: int) -> None:
    while value in dq:
        dq.remove(value)
