from typing import Optional, Set


class Node:
    def __init__(self, value: int, next: Optional['Node'] = None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value)


def print_linked_list(head: Node) -> None:
    current = head
    while current:
        print(current.value, end=' ')
        current = current.next


def remove_duplicates(head: Node) -> Node:
    if not head:
        return head

    seen: Set[int] = set()
    dummy = Node(0, head)  # Вспомогательный узел перед головой
    prev = dummy
    current = head

    while current:
        if current.value in seen:
            # Удаляем текущий узел - связываем prev с current.next
            prev.next = current.next
            # current не обновляем prev, только сдвигаем current
        else:
            seen.add(current.value)
            prev = current

        current = current.next

    return dummy.next


head = Node(1, Node(1, Node(1, Node(1, Node(1)))))
print_linked_list(remove_duplicates(head))
head = Node(1, Node(2, Node(1, Node(3, Node(2)))))
print_linked_list(remove_duplicates(head))
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print_linked_list(remove_duplicates(head))
