from typing import List, Optional, Tuple


class Node:
    def __init__(self, value: int, next: Optional['Node'] = None) -> None:
        self.value: int = value
        self.next: Optional['Node'] = next

    def __repr__(self):
        return str(self.value)


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


def insert(head: Node, k: int) -> Node:
    node = Node(k)

    if head.next is head:
        if k < head.value:
            node.next = head
            head.next = node
            return node
        else:
            head.next = node
            head.next.next = head
            return head

    current = head.next
    prev_node = head

    while current is not head:
        if current.value >= k and prev_node.value <= k:
            prev_node.next = node
            node.next = current
            return head
        prev_node = current
        current = current.next

    if k >= prev_node.value:
        prev_node.next = node
        node.next = head
        return head
    elif k <= head.value:
        node.next = head
        prev_node.next = node
        return node


def is_cycled(head: Node) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


head = convert_circular([1, 2, 3, 5])
print_circular_linked_list(insert(head, 4))

head = convert_circular([-5, -4, -3, -2])
print_circular_linked_list(insert(head, -1))

head = convert_circular([1])
print_circular_linked_list(insert(head, 0))

head = convert_circular([4, 4, 4, 4])
print_circular_linked_list(insert(head, 4))

head = convert_circular([0, 1, 2])
print_circular_linked_list(insert(head, -1))
