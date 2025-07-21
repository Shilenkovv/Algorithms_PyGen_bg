class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size: int = 0

    def enqueue(self, elem: int):
        new_node = Node(elem)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Очередь пуста')
        dequeued_node = self.head
        self.head = dequeued_node.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return dequeued_node.value

    def peek(self):
        if self.is_empty():
            raise IndexError('Очередь пуста')
        return self.head.value

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size


class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        # Просто добавляем элемент в первую очередь, O(1)
        self.q1.enqueue(x)

    def pop(self):
        # Перекладываем все, кроме последнего, из q1 в q2
        # Последний элемент в q1 — вершина стека
        while self.q1.size() > 1:
            self.q2.enqueue(self.q1.dequeue())

        # Последний элемент — это элемент для возврата
        popped = self.q1.dequeue()

        # Меняем очереди местами, чтобы q1 снова была основной очередью
        self.q1, self.q2 = self.q2, self.q1

        return popped
