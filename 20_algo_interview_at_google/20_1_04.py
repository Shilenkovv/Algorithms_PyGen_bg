from typing import List, Optional, Tuple


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


def split(head: Optional[Node]) -> Tuple[Node, Node]:
    head_odd = Node(0)
    head_even = Node(0)
    cur_odd = head_odd
    cur_even = head_even

    n = 0
    current = head
    while current:
        n += 1
        if n % 2:
            cur_odd.next = current
            cur_odd = cur_odd.next
        else:
            cur_even.next = current
            cur_even = cur_even.next
        current = current.next
    cur_odd.next = None
    cur_even.next = None
    return (head_odd.next, head_even.next)


head1 = Node(10, Node(20, Node(30, Node(40, Node(50, Node(60))))))
head2, head3 = split(head1)
print_linked_list(head2)
print()
print_linked_list(head3)
