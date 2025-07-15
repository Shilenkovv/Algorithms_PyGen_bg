from typing import List, Optional


class Node:
    def __init__(self, value: int, next: Optional['Node'] = None) -> None:
        self.value: int = value
        self.next: Optional['Node'] = next
        self.prev: Optional['Node'] = next


def print_linked_list(head: Node, reverse: bool = False):
    if not reverse:
        current = head
        while current:
            print(current.value, end=' ')
            current = current.next
    else:
        current = head
        while current.next:
            current = current.next
        while current:
            print(current.value, end=' ')
            current = current.prev


def convert(nums: List[int]) -> Node:
    prev_node = Node(nums[0])
    prev_node.prev = None
    head = prev_node

    for i in range(1, len(nums)):
        cur_node = Node(nums[i])
        cur_node.prev = prev_node
        prev_node.next = cur_node
        prev_node = cur_node
    return head


def get_tail(head: Node) -> Node:
    tail = head
    while tail.next:
        tail = tail.next
    return tail


def pretty_print_reverse(tail: Node) -> None:
    cur_node = tail
    while cur_node.prev is not None:
        print(cur_node.value, ' <-> ', sep='', end='')
        cur_node = cur_node.prev
    print(cur_node.value)


def length(node: Node) -> int:
    cnt = -1

    cur_node = node
    while cur_node:
        cnt += 1
        cur_node = cur_node.next

    cur_node = node
    while cur_node:
        cnt += 1
        cur_node = cur_node.prev
    return cnt


head = convert([1, 2, 3, 4, 5])
pretty_print_reverse(get_tail(head))
