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
    print()


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


def reverse(head: Node) -> Node:
    if head.next is None:
        return head

    current = head
    new_head = None

    while current:
        current.prev, current.next = current.next, current.prev
        new_head = current
        current = current.prev

    return new_head


def swap_pairs(head: Node) -> Node:
    if not head or not head.next:
        return head  # Если список пуст или один узел, ничего менять не надо

    current = head
    new_head = head.next  # Новый голова — второй элемент после первой перестановки

    while current and current.next:
        first = current
        second = current.next
        next_pair = second.next

        # Меняем ссылки между first и second
        second.prev = first.prev
        first.next = next_pair

        if next_pair:
            next_pair.prev = first

        second.next = first
        first.prev = second

        # Если есть предыдущая пара, скрепляем её с текущей
        if second.prev:
            second.prev.next = second

        # Переходим к следующей паре
        current = next_pair

    return new_head


def remove(head: Node, k: int) -> Node:
    if head.value == k:
        while head.value == k:
            head = head.next
        head.prev = None
    current = head

    while current:
        if current.value != k:
            last_non_k_node = current
        elif current.value == k:
            while current and current.value == k:
                current = current.next
            if current:
                last_non_k_node.next = current
                current.prev = last_non_k_node
                last_non_k_node = current
            else:
                last_non_k_node.next = None
                return head
        current = current.next
    return head


def remove_every_kth(head: Node, k: int) -> Node:
    if k <= 1:  # Если k = 1 или меньше, удаляем весь список
        return None

    current = head
    position = 1  # Нумерация с 1

    while current:
        next_node = current.next

        if position % k == 0:
            # Удаляем current
            if current.prev:
                current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev

            # Если удаляем голову
            if current == head:
                head = current.next

        current = next_node
        position += 1

    return head


head = convert([1, 2, 3, 4, 5])
print_linked_list(remove_every_kth(head, 2))
