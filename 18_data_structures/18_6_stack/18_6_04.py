from typing import List


class CustomStack:
    def __init__(self, size: int):
        self.size = size
        self.stack: List[int] = []

    def push(self, num: int) -> None:
        if len(self.stack) < self.size:
            self.stack.append(num)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def inc(self, k: int, n: int) -> None:
        if len(self.stack) < k:
            for i in range(len(self.stack)):
                self.stack[i] += n
        else:
            for i in range(k):
                self.stack[i] += n


stack = CustomStack(3)
stack.push(1)  # [1]
stack.push(2)  # [1, 2]
stack.push(3)  # [1, 2, 3]
stack.push(4)  # [1, 2, 3]
stack.inc(2, 10)  # [11, 12, 3]
print(stack.pop())  # [11, 12]
print(stack.pop())  # [11]
print(stack.pop())  # []
