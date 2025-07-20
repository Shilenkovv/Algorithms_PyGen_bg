from math import ceil
from typing import List


class SetOfStacks:
    def __init__(self, size: int):
        self.stack: List[int] = []
        self.size = size
        self.cur_size = 0

    def push(self, num: int) -> None:
        self.stack.append(num)
        self.cur_size += 1

    def pop(self) -> int | None:
        if self.stack:
            elem = self.stack.pop()
            self.cur_size -= 1
            return elem

    def stacks(self) -> int:
        return ceil(self.cur_size / self.size)

    def peek_at(self, i: int) -> int:
        if self.size * (i + 1) <= self.cur_size:
            return self.stack[self.size * (i + 1) - 1]
        else:
            return self.stack[self.cur_size - 1]


# stack = SetOfStacks(2)
# stack.push(1)  # [1]
# stack.push(2)  # [1, 2]
# stack.push(3)  # [1, 2] [3]
# stack.push(4)  # [1, 2] [3, 4]
# stack.push(5)  # [1, 2] [3, 4] [5]
# print(stack.pop())  # [1, 2] [3, 4]
# print(stack.pop())  # [1, 2] [3]

# stack = SetOfStacks(2)
# stack.push(1)  # [1]
# stack.push(2)  # [1, 2]
# stack.push(3)  # [1, 2] [3]
# stack.push(4)  # [1, 2] [3, 4]
# print(stack.peek_at(0))  # 2
# print(stack.peek_at(1))  # 4

stack = SetOfStacks(2)
print(stack.stacks())  # 0
stack.push(1)  # [1]
stack.push(2)  # [1, 2]
stack.push(3)  # [1, 2] [3]
stack.push(4)  # [1, 2] [3, 4]
print(stack.stacks())  # 2
stack.pop()  # [1, 2] [3]
stack.pop()  # [1, 2]
print(stack.stacks())  # 1

stack = SetOfStacks(1)
stack.push(1)  # [1]
stack.push(2)  # [2]
stack.push(3)  # [3]
stack.push(4)  # [4]
stack.push(5)  # [5]
print(stack.stacks())  # 5
print(stack.peek_at(0))  # 1
print(stack.peek_at(1))  # 2
print(stack.peek_at(2))  # 3
print(stack.peek_at(3))  # 4
print(stack.peek_at(4))  # 5
