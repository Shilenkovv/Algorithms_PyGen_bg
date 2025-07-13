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


head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
pretty_print(head)
