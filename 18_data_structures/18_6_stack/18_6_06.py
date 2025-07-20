from typing import List


class TwoStacks:
    def __init__(self, size: int):
        self.stack: List[int] = [0] * size * 2
        self.size = size
        self.len1 = 0
        self.len2 = 0

    def push1(self, num: int) -> None:
        if self.len1 + self.len2 < self.size:
            self.stack[self.len1] = num
            self.len1 += 1

    def push2(self, num: int) -> None:
        if self.len1 + self.len2 < self.size:
            self.stack[self.len2 + self.size] = num
            self.len2 += 1

    def pop1(self) -> int | None:
        if self.len1 != 0:
            self.len1 -= 1
            return self.stack[self.len1]
        return -1

    def pop2(self) -> int | None:
        if self.len2 != 0:
            self.len2 -= 1
            return self.stack[self.size + self.len2]
        return -1


stack = TwoStacks(3)
stack.push1(1)  # [1]
stack.push1(2)  # [1, 2]
stack.push1(3)  # [1, 2, 3]
stack.push2(4)  # []
print(stack.pop1())  # [1, 2]
print(stack.pop2())  # []
