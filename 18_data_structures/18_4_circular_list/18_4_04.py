from typing import List, Optional


class Node:
    def __init__(
        self, value: int, next: Optional['Node'] = None, prev: Optional['Node'] = None
    ) -> None:
        self.value: int = value
        self.next: Optional['Node'] = next


def convert(data: List[int]):
    head = Node(0)
    current = head
    for elem in data:
        current.next = Node(elem)
        current = current.next
    return head.next


def convert_circular(data: List[int]):
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


def length(head: Node) -> int:
    if head.next is None:
        return 1

    cur_len = 1
    current = head.next

    while current is not head:
        cur_len += 1
        current = current.next
    return cur_len


def is_circular(head: Node) -> bool:
    current = head

    while current:
        if current.next is head:
            return True
        if current.next is None:
            return False
        current = current.next


head = convert([1, 2, 3, 4, 5])
print(is_circular(head))

head = convert_circular([1, 2, 3, 4, 5])
print(is_circular(head))
