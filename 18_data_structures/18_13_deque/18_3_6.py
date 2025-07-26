from collections import deque


class MidDeque:
    def __init__(self):
        self.left: deque[int] = deque()
        self.right: deque[int] = deque()

    def _rebalance(self):
        # Инвариант: len(left) >= len(right) и разница не более 1
        while len(self.left) > len(self.right) + 1:
            self.right.appendleft(self.left.pop())
        while len(self.left) < len(self.right):
            self.left.append(self.right.popleft())

    def push_front(self, x: int):
        self.left.appendleft(x)
        self._rebalance()

    def push_back(self, x: int):
        self.right.append(x)
        self._rebalance()

    def push_mid(self, x: int):
        if len(self.left) != len(self.right):
            self.right.appendleft(self.left.pop())
        self.left.append(x)

        self._rebalance()

    def pop_front(self):
        if self.left:
            val = self.left.popleft()
        else:
            val = self.right.popleft()
        self._rebalance()
        return val

    def pop_back(self):
        if self.right:
            val = self.right.pop()
        else:
            val = self.left.pop()
        self._rebalance()
        return val

    def pop_mid(self):
        val = self.left.pop()  # всегда удаляем из "левой середины"
        self._rebalance()
        return val


# dq = MidDeque()
# dq.push_back(1)  # [1]
# dq.push_mid(2)  # [2, 1]
# dq.push_mid(3)  # [2, 3, 1]
# dq.push_mid(-1)  # [2, -1, 3, 1]
# print(dq.pop_front())
# print(dq.pop_front())
# print(dq.pop_front())
# print(dq.pop_front())
