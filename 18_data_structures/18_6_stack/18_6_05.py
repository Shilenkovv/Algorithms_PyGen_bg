from typing import List


class MinStack:
    def __init__(self):
        self.stack: List[int] = []
        self.min_stack: List[int] = []

    def push(self, num: int) -> None:
        self.stack.append(num)
        if not self.min_stack or num <= self.min_stack[-1]:
            self.min_stack.append(num)

    def pop(self) -> int:
        if not self.stack:
            raise Exception('Stack is empty')
        val = self.stack.pop()
        # Pop from min_stack if it matches the popped value
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def get_min(self) -> int:
        if not self.min_stack:
            raise Exception('Stack is empty')
        return self.min_stack[-1]


# stack = MinStack()
# stack.push(3)  # [3]
# stack.push(5)  # [3, 5]
# stack.push(2)  # [3, 5, 2]
# print(stack.get_min())  # 2
# stack.pop()  # [3, 5]
# print(stack.get_min())  # 3


# stack = MinStack()
# stack.push(4)  # [4]
# stack.push(-3)  # [4, -3]
# stack.push(-2)  # [4, -3, -2]
# print(stack.get_min())  # -3
# stack.pop()  # [4, -3]
# print(stack.get_min())  # -3
# stack.pop()  # [4]
# print(stack.get_min())  # 4
