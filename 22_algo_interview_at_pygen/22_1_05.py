from collections import deque
from typing import List, Optional


class Node:
    def __init__(self, value: int, next: Optional['Node'] = None) -> None:
        self.value: int = value
        self.next: Optional['Node'] = next

    def __repr__(self) -> str:
        return str(self.value)


def convert(data: List[int]) -> Optional[Node]:
    head = Node(0)
    current = head
    for elem in data:
        current.next = Node(elem)
        current = current.next
    return head.next


def print_linked_list(head: Optional[Node]) -> None:
    current = head
    while current:
        print(current.value, end=' ')
        current = current.next


def partition_by(head: Node, k: int) -> Node:
    less: deque[Node] = deque()
    equal: deque[Node] = deque()
    higher: deque[Node] = deque()

    current = head
    while current:
        if current.value < k:
            less.append(current)
        elif current.value == k:
            equal.append(current)
        else:
            higher.append(current)
        current = current.next

    new_head = Node(0)
    current = new_head

    while less:
        tmp_node = less.popleft()
        tmp_node.next = None
        current.next = tmp_node
        current = current.next
    while equal:
        tmp_node = equal.popleft()
        tmp_node.next = None
        current.next = tmp_node
        current = current.next
    while higher:
        tmp_node = higher.popleft()
        tmp_node.next = None
        current.next = tmp_node
        current = current.next

    return new_head.next


# head = Node(-1, Node(-2, Node(-3, Node(-4, Node(-5)))))
# print_linked_list(partition_by(head, -3))
