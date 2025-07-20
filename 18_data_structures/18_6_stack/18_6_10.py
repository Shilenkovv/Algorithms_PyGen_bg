from typing import List


class Stack:
    def __init__(self):
        self.stack: List[int] = []

    def push(self, elem: int):
        self.stack.append(elem)

    def pop(self):
        if self.is_empty():
            raise IndexError('Стек пуст')
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError('Стек пуст')
        return self.stack[-1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.stack)

    def print(self):
        for elem in self.stack:
            print(elem, end=' ')


def convert(data: List[int]) -> Stack:
    stack = Stack()
    for elem in data:
        stack.push(elem)
    return stack


def sort_stack(stack: Stack) -> Stack:
    sorted_stack = Stack()

    while not stack.is_empty():
        tmp = stack.pop()

        # Перемещение элементов из sorted_stack обратно в stack,
        # если они больше tmp
        while not sorted_stack.is_empty() and sorted_stack.peek() > tmp:
            stack.push(sorted_stack.pop())

        sorted_stack.push(tmp)

    return sorted_stack


stack1 = convert([3, 2, 5, 1, 4])
stack2 = sort_stack(stack1)
stack2.print()
