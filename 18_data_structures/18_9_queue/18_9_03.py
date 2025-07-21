from typing import List


class Queue:
    def __init__(self):
        self.stack1: List[int | str] = []
        self.stack2: List[int | str] = []

    def enqueue(self, elem: int | str) -> None:
        if not self.stack1 and not self.stack2:
            self.stack1.append(elem)
        elif not self.stack2 and self.stack1:
            self.stack2.append(elem)
            while self.stack1:
                self.stack2.append(self.stack1.pop(0))
        elif not self.stack1 and self.stack2:
            self.stack1.append(elem)
            while self.stack2:
                self.stack1.append(self.stack2.pop(0))

    def dequeue(self):
        if self.stack1 and not self.stack2:
            return self.stack1.pop()
        elif self.stack2 and not self.stack1:
            return self.stack2.pop()


# queue = Queue()
# queue.enqueue(1)  # [1]
# queue.enqueue(2)  # [1, 2]
# queue.enqueue(3)  # [1, 2, 3]
# print(queue.dequeue())  # [2, 3]
# print(queue.dequeue())  # [3]
# print(queue.dequeue())  # []

queue = Queue()
queue.enqueue(1)  # [1]
print(queue.dequeue())  # []
queue.enqueue(2)  # [2]
print(queue.dequeue())  # []
queue.enqueue(3)  # [3]
print(queue.dequeue())  # []

queue = Queue()
queue.enqueue(-2)  # [-2]
queue.enqueue(4)  # [-2, 4]
print(queue.dequeue())  # [4]
queue.enqueue(-3)  # [4, -3]
queue.enqueue(0)  # [4, -3, 0]
print(queue.dequeue())  # [-3, 0]
print(queue.dequeue())  # [0]
print(queue.dequeue())  # []

queue = Queue()
queue.enqueue(10)  # [10]
queue.enqueue(20)  # [10, 20]
queue.enqueue(30)  # [10, 20, 30]
print(queue.dequeue())  # [20, 30]
print(queue.dequeue())  # [30]
queue.enqueue(40)  # [30, 40]
queue.enqueue(50)  # [30, 40, 50]
print(queue.dequeue())  # [40, 50]
print(queue.dequeue())  # [50]
print(queue.dequeue())  # []

queue = Queue()
queue.enqueue('a')  # ['a']
print(queue.dequeue())  # []
queue.enqueue(2)  # [2]
queue.enqueue('3')  # [2, '3']
print(queue.dequeue())  # ['3']
queue.enqueue('c')  # ['3', 'c']
print(queue.dequeue())  # ['c']
print(queue.dequeue())  # []
