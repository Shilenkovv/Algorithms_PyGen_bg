class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


head = Node('a', Node('b', Node('c', Node('d'))))
