from collections import deque


def rotate(exp: str, k: int) -> str:
    deq = deque(exp)
    deq.rotate(k)
    return ''.join(deq)


print(rotate('python', 1))
print(rotate('python', 2))
print(rotate('python', -3))
print(rotate('python', 0))
