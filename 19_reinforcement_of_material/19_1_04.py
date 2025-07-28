from typing import Optional


class Node:
    def __init__(self, value: int, next: Optional['Node'] = None):
        self.value = value
        self.next = next


def sort_linked_list(head: Node) -> Node:
    count = [0, 0, 0]
    current = head

    # Подсчёт количества 0, 1, 2
    while current:
        count[current.value] += 1
        current = current.next

    current = head
    i = 0

    # Перезапись значений в списке в отсортированном порядке
    while current:
        if count[i] == 0:
            i += 1
        else:
            current.value = i
            count[i] -= 1
            current = current.next

    return head
