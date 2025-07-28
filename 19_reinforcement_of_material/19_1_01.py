from typing import List, Optional


class Node:
    def __init__(self, value: int, next: Optional['Node'] = None):
        self.value = value
        self.next = next


def convert(data: List[int]):
    head = Node(0)
    current = head
    for elem in data:
        current.next = Node(elem)
        current = current.next
    return head.next


def in_order(head: Node) -> bool:
    if head.next is None or (head.next.next is None and head.value != head.next.value):
        return True
    ascending = False

    if head.next.value == head.value:
        return False
    elif head.next.value > head.value:
        ascending: bool = True

    cur_node = head
    while cur_node.next is not None:
        if any(
            [
                cur_node.next.value < cur_node.value and ascending,
                cur_node.next.value > cur_node.value and not ascending,
                cur_node.value == cur_node.next.value,
            ]
        ):
            return False
        cur_node = cur_node.next
    return True
