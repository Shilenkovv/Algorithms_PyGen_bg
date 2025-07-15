from typing import Optional


class Node:
    def __init__(
        self, value: int, next: Optional['Node'] = None, prev: Optional['Node'] = None
    ) -> None:
        self.value: int = value
        self.next: Optional['Node'] = next
        self.prev: Optional['Node'] = prev


def convert(data):
    head = Node(0)
    current = head
    for elem in data:
        current.next = Node(elem)
        current = current.next
    current.next = head.next
    return head.next


def print_circular_linked_list(head: Node):
    current = head
    print(current.value, end=' ')
    current = current.next
    while current is not head:
        print(current.value, end=' ')
        current = current.next
    print()


node1 = Node(2)
node2 = Node(3)
node3 = Node(5)
node1.next, node2.next, node3.next = node2, node3, node1
node1.prev, node2.prev, node3.prev = node3, node1, node2
head = node1
