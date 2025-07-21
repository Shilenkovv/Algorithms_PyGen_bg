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


def time_required(tickets: List[int], k: int) -> int:
    tickets_needed = tickets[k - 1]
    ans = 0
    n = len(tickets) if tickets_needed != 1 else k
    for i in range(n):
        if i <= k - 1:
            ans += min(tickets[i], tickets_needed)
        else:
            ans += min(tickets[i], tickets_needed - 1)
    return ans


# print(time_required([1, 1, 1], 3))  # 3
# print(time_required([2, 3, 2], 2))  # 7
# print(time_required([5], 1))  # 5
# print(time_required([5, 3, 1], 1))  # 9
# print(time_required([5, 3, 100], 1))  # 13
# print(time_required([4, 2, 1, 3, 4], 3))  # 3
# print(time_required([2, 2, 2], 2)) # 5
