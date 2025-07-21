from typing import List


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size: int = 0

    def enqueue(self, elem: int):
        new_node = Node(elem)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Очередь пуста')
        dequeued_node = self.head
        self.head = dequeued_node.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return dequeued_node.value

    def peek(self):
        if self.is_empty():
            raise IndexError('Очередь пуста')
        return self.head.value

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size


def can_sort(queue: Queue):
    stack: List[int] = []
    expected = 1
    n = queue.size()

    while not queue.is_empty() or stack:
        if stack and stack[-1] == expected:
            stack.pop()
            expected += 1
        elif not queue.is_empty():
            val = queue.dequeue()
            if val == expected:
                expected += 1
            else:
                stack.append(val)
        else:
            # Не можем получить следующий ожидаемый элемент
            return False
    return expected == n + 1
