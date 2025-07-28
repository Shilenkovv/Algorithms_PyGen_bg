from typing import Optional


class Node:
    def __init__(self, value: int, next: Optional['Node'] = None):
        self.value = value
        self.next = next


def reverse(head: Node, a: int, b: int) -> Node:
    if a == b:
        return head  # Нечего переворачивать

    dummy = Node(0, head)  # Вспомогательный узел перед головой списка
    prev_a = dummy

    # Найдем узел перед a-ым индексом (prev_a)
    for _ in range(a):
        prev_a = prev_a.next

    # start - первый узел подсписка для переворота
    start = prev_a.next
    then = start.next

    # Перевернем подсписок размером (b - a)
    for _ in range(b - a):
        start.next = then.next
        then.next = prev_a.next
        prev_a.next = then
        then = start.next

    return dummy.next
