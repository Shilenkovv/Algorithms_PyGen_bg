from typing import List, Optional


class Node:
    def __init__(self, value: int, next: Optional['Node'] = None) -> None:
        self.value: int = value
        self.next: Optional['Node'] = next


def print_linked_list(head: Node) -> None:
    current = head
    while current:
        print(current.value, end=' ')
        current = current.next


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


def get_node(head: Node, index: int):
    current_node = head
    for _ in range(index):
        current_node = current_node.next
    return current_node.value


def get_last_value(head: Node) -> int:
    cur_node = head
    while cur_node.next:
        cur_node = cur_node.next
    return cur_node.value


def replace(head: Node, index: int, k: int) -> None:
    if index == 0:
        head.value = k

    cur_idx = 0
    cur_node = head
    while cur_idx != index:
        cur_idx += 1
        cur_node = cur_node.next
    cur_node.value = k


def print_reverse(head: Node) -> None:
    if head is not None:  # проверяем, что текущий узел не равен None
        print_reverse(head.next)
        print(head.value, end=' ')  # выводим значение текущего узла


def extend(head1: Node, head2: Node) -> None:
    cur_node = head1
    while cur_node.next:
        cur_node = cur_node.next
    cur_node.next = head2


head1 = Node(1, Node(2, Node(3)))
head2 = Node(4, Node(5))
extend(head1, head2)
print_linked_list(head1)
