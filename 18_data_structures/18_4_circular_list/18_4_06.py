from typing import List, Optional, Tuple


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


def swap_head_and_tail(head: Node) -> Node:
    if head.next == head:
        return head

    current = head.next
    prev_node = head

    while current.next is not head:
        prev_node = current
        current = current.next

    prev_node.next = head
    current.next = head.next
    head.next = current
    return current


def split(head: Node) -> Tuple[Node, Node]:
    length = 1

    current = head.next

    while current is not head:
        length += 1
        current = current.next

    current = head

    for _ in range(length // 2 - 1):
        current = current.next

    head2 = current.next
    current.next = head

    current = head2
    for _ in range(length // 2 - 1):
        current = current.next
    current.next = head2

    return (head, head2)


head1 = convert_circular([1, 2, 3, 4, 5, 6])
head2, head3 = split(head1)
print_circular_linked_list(head2)
print()
print_circular_linked_list(head3)
