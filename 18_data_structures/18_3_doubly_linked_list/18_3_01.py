from typing import Optional


class Node:
    def __init__(self, value: int, next: Optional['Node'] = None) -> None:
        self.value: int = value
        self.next: Optional['Node'] = next
        self.prev: Optional['Node'] = next


node1 = Node(-10)
node2 = Node(0)
node3 = Node(10)

node1.next = node2
node2.prev = None
node2.next = node3
node2.prev = node1
node3.next = None
node3.prev = node2
