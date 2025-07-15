from typing import Optional


class Node:
    def __init__(self, value: int, next: Optional['Node'] = None) -> None:
        self.value: int = value
        self.next: Optional['Node'] = next


node1 = Node('a')
node2 = Node('b')
node3 = Node('c')
node1.next = node2
node2.next = node3
node3.next = node1
