from typing import List, Optional


class Node:
    def __init__(self, value: int, next: Optional['Node'] = None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value)


def convert(data: List[int]) -> Node:
    head = Node(0)
    current = head
    for elem in data:
        current.next = Node(elem)
        current = current.next
    return head.next


def print_linked_list(head: Node) -> None:
    current = head
    while current:
        print(current.value, end=' ')
        current = current.next


def repr_linked_list(head: Node) -> str:
    cur_list: List[str] = []
    current = head
    n = 0
    while current:
        cur_list.append(f'Node({current.value}')
        n += 1
        current = current.next
    return ', '.join(cur_list) + ')' * n


head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(repr_linked_list(head))

head = Node(1)
print(repr_linked_list(head))
