from typing import List, Optional


class Node:
    def __init__(self, value: int, next: Optional['Node'] = None) -> None:
        self.value: int = value
        self.next: Optional['Node'] = next


def pretty_print(head: Optional[Node]) -> None:
    current = head
    while current:
        print(current.value, end='')
        if current.next is not None:
            print(' -> ', end='')
        current = current.next
    print()  # Для переноса строки после вывода


def convert(nums: List[int]) -> Optional[Node]:
    if not nums:
        return None
    head = Node(nums[0])
    cur_node = head
    for i in range(1, len(nums)):
        cur_node.next = Node(nums[i])
        cur_node = cur_node.next
    return head


def length(head: Node) -> int:
    tot_len = 1
    cur_node = head
    while cur_node.next:
        tot_len += 1
        cur_node = cur_node.next
    return tot_len


def get_last_value(head: Node) -> int:
    cur_node = head
    while cur_node.next:
        cur_node = cur_node.next
    return cur_node.value


head = Node(1)
print(get_last_value(head))
