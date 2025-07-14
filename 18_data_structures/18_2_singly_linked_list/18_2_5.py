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
    print()


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


def leave_first_and_last(head: Node) -> None:
    cur_node = head
    if cur_node.next is None:
        return
    while cur_node.next:
        cur_node = cur_node.next
    head.next = cur_node


def remove_prev_to_last(head: Node) -> Node:
    if head.next.next is None:
        head = head.next
        return head
    else:
        cur_node = head
        while cur_node.next.next.next:
            cur_node = cur_node.next
        cur_node.next = cur_node.next.next
        return head


def insert_zeroes(head: Node) -> None:
    if head.next is not None:
        prev = head
        while prev.next:
            prev.next = Node(0, prev.next)
            prev = prev.next.next


def remove_zeroes(head: Optional[Node]) -> Optional[Node]:
    # Удаляем все ведущие нули
    while head is not None and head.value == 0:
        head = head.next

    # Если список опустел после удаления нулей
    if head is None:
        return None

    current = head
    while current.next is not None:
        if current.next.value == 0:
            # Пропускаем все нули подряд
            skip = current.next
            while skip is not None and skip.value == 0:
                skip = skip.next
            current.next = skip
        else:
            current = current.next

    return head


def remove_min_max(head: Node) -> Node:
    min_val = float('inf')
    max_val = -float('inf')

    cur_node = head
    while cur_node is not None:
        if cur_node.value > max_val:
            max_val = cur_node.value
        if cur_node.value < min_val:
            min_val = cur_node.value
        cur_node = cur_node.next

    min_found, max_found = False, False

    cur_node = head
    while cur_node.value == max_val or cur_node.value == min_val:
        if cur_node.value == max_val:
            max_found = True
            head = cur_node.next
            cur_node = head
        if cur_node.value == min_val:
            min_found = True
            head = cur_node.next
            cur_node = head

    if cur_node is None:
        return None

    while cur_node is not None and cur_node.value is not None:
        while cur_node.next is not None and (
            cur_node.next.value == min_val or cur_node.next.value == max_val
        ):
            if not min_found and cur_node.next.value == min_val:
                min_found = True
                cur_node.next = cur_node.next.next
            if not max_found and cur_node.next.value == max_val:
                max_found = True
                cur_node.next = cur_node.next.next
        cur_node = cur_node.next
    return head


def group_odd_even(head: Node) -> Node:
    if head is None or head.next is None:
        return head

    even_head = head  # узлы с индексами 0, 2, 4, ...
    odd_head = head.next  # узлы с индексами 1, 3, 5, ...

    even = even_head
    odd = odd_head

    cur_node = head.next.next
    index = 2  # текущий индекс узла

    while cur_node:
        if index % 2 == 0:  # чётный индекс
            even.next = cur_node
            even = even.next
        else:  # нечётный индекс
            odd.next = cur_node
            odd = odd.next
        cur_node = cur_node.next
        index += 1

    even.next = odd_head
    odd.next = None

    return even_head


def insert(head: Node, k: int) -> Node:
    if k < head.value:
        head = Node(k, head)
        return head
    cur_node = head
    while cur_node.next is not None:
        if k >= cur_node.value and k <= cur_node.next.value:
            k_node = Node(k, cur_node.next)
            cur_node.next = k_node
            return head
        cur_node = cur_node.next
    if k >= cur_node.value:
        cur_node.next = Node(k, None)
    return head


def are_equal(head1: Node, head2: Node) -> bool:
    cur_node1 = head1
    cur_node2 = head2

    while cur_node1 is not None and cur_node2 is not None:
        if cur_node1.value != cur_node2.value:
            return False
        cur_node1 = cur_node1.next
        cur_node2 = cur_node2.next
    return True if cur_node1 is None and cur_node2 is None else False


head1 = Node(1, Node(2, Node(3)))
head2 = Node(1, Node(2, Node(3)))
print(are_equal(head1, head2))  # True

head1 = Node(1, Node(2, Node(3)))
head2 = Node(1, Node(2, Node(3, Node(4))))
print(are_equal(head1, head2))  # False

head1 = Node(1, Node(2, Node(3, Node(4))))
head2 = Node(4, Node(3, Node(2, Node(1))))
print(are_equal(head1, head2))  # False

head1 = convert([1, 2, 3, 4])
head2 = convert([1, 2, 3, 4, 5])
print(are_equal(head1, head2))  # False
