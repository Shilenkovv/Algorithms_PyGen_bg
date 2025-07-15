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


def print_linked_list(head: Node) -> None:
    current = head
    while current:
        print(current.value, end=' ')
        current = current.next
    print()


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

    while current is not head and current is not None:
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


def rotate(head: Node, k: int) -> Node:
    list_len = length(head)
    if k % list_len == 0:
        return head

    should_start_idx = k % list_len

    current = head
    for _ in range(should_start_idx - 1):
        current = current.next

    head_new = current.next
    current.next = None

    current = head_new
    while current.next is not None:
        current = current.next
    current.next = head

    return head_new


def remove_and_reverse(head: Node, k: int) -> Node:
    if head.next == head:
        return head

    cur_len = length(head)

    if head.value == k:
        current = head.next
        while current.next is not head:
            current = current.next
        current.next = head.next
        head = head.next
    else:
        prev_node = head
        current = head.next

        while current is not head:
            if current.value == k:
                cur_len -= 1
                prev_node.next = current.next
                break
            prev_node = current
            current = current.next
    # else:
    #     if head.value == k:
    #         cur_len -= 1
    #         current.next = head.next
    #         head = current.next

    if cur_len == 1:
        return head

    prev_node = head
    current = head.next

    while current is not head:
        next_node = current.next
        current.next = prev_node
        prev_node = current
        current = next_node
    current.next = prev_node
    return prev_node


def josephus(n: int, k: int) -> int:
    if k == 1:
        return n
    if n == 1:
        return 1
    if n == 2:
        return 1 if k % 2 == 0 else 2
    head = convert_circular(list(range(1, n + 1)))

    current = head.next
    prev_node = head
    cnt = 2

    while prev_node is not current:
        if cnt % k == 0:
            prev_node.next = current.next
        else:
            prev_node = current
        current = current.next
        cnt += 1
    return current.value


print(josephus(13, 3))

head = convert_circular([0, 4, 2])
print_circular_linked_list(remove_and_reverse(head, 0))

head = convert_circular([1, 2])
print_circular_linked_list(remove_and_reverse(head, 2))

head = convert_circular([1, 2, 3, 4, 5])
print_circular_linked_list(remove_and_reverse(head, 6))

head = convert_circular([1, 2, 3, 4, 5])
print_circular_linked_list(remove_and_reverse(head, 2))
