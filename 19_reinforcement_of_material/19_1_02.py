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


def remove_kth_from_end(head: Node, k: int) -> Node:
    n = 1
    cur_node = head
    while cur_node.next is not None:
        n += 1
        cur_node = cur_node.next
    if n == k and head.next is not None:
        head = head.next
        return head

    rmv_idx = n - k + 1
    j = 1

    cur_node = head
    while j != rmv_idx - 1:
        j += 1
        cur_node = cur_node.next
    if cur_node.next.next is None:
        cur_node.next = None
        return head
    cur_node.next = cur_node.next.next
    return head


head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
head = remove_kth_from_end(head, 2)
print_linked_list(head)
