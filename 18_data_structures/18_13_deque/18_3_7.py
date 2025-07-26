from collections import deque


class MinQueue:
    def __init__(self):
        self.data: deque[int] = deque()  # основная очередь
        self.minq: deque[int] = deque()  # очередь для минимума

    def enqueue(self, x: int):
        self.data.append(x)
        while self.minq and self.minq[-1] > x:
            self.minq.pop()
        self.minq.append(x)

    def dequeue(self) -> int:
        val = self.data.popleft()
        if val == self.minq[0]:
            self.minq.popleft()
        return val

    def get_min(self) -> int:
        return self.minq[0]


queue = MinQueue()
queue.enqueue(2)  # [2]
queue.enqueue(1)  # [2, 1]
queue.enqueue(3)  # [2, 1, 3]
print(queue.get_min())
