from typing import List, Optional


class Node:
    def __init__(self, value: int, next: Optional['Node'] = None) -> None:
        self.value: int = value
        self.next: Optional['Node'] = next
        self.prev: Optional['Node'] = next


def print_linked_list(head: Node, reverse=False):
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


nums = [1, 5, 10]
h = convert(nums)
print(h.value, h.next, h.prev)


node1 = Node(-10)
node2 = Node(0)
node3 = Node(10)

node1.next = node2
node2.prev = None
node2.next = node3
node2.prev = node1
node3.next = None
node3.prev = node2

head = node1
