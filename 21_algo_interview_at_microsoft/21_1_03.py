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


def intersection(head1: Node, head2: Node) -> Node:
    cur1 = head1
    cur2 = head2
    new_head = Node(0)
    new_cur = new_head
    while cur1 and cur2:
        if cur1.value == cur2.value:
            new_cur.next = Node(cur1.value)
            new_cur = new_cur.next
            cur1 = cur1.next
            cur2 = cur2.next
        elif cur1.value > cur2.value:
            cur2 = cur2.next
        else:
            cur1 = cur1.next
    return new_head.next


# head1 = Node(1, Node(2, Node(3)))
# head2 = Node(2, Node(3, Node(4, Node(5))))
# print_linked_list(intersection(head1, head2))  # 2 3

# head1 = Node(0, Node(1, Node(3, Node(5))))
# head2 = Node(0, Node(2, Node(4, Node(4))))
# print_linked_list(intersection(head1, head2))  # 0

# head1 = Node(1, Node(1, Node(2, Node(2))))
# head2 = Node(1, Node(1, Node(2, Node(2))))
# print_linked_list(intersection(head1, head2))  # 1 1 2 2
