class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        return str(self.val)


class MidStack:
    def __init__(self):
        self.head = None
        self.mid = None
        self.size = 0

    def push(self, x):
        node = Node(x)
        node.prev = self.head
        if self.head:
            self.head.next = node
        self.head = node
        self.size += 1
        if self.size == 1:
            self.mid = node
        else:
            if self.size == 2 or self.size % 2 == 0:
                self.mid = self.mid.next

    def pop(self):
        if self.size == 0:
            raise IndexError('pop from empty stack')
        res = self.head.val
        self.head = self.head.prev
        if self.head:
            self.head.next = None
        self.size -= 1
        if self.size == 0:
            self.mid = None
        elif self.size % 2 == 1:
            self.mid = self.mid.prev
        return res

    def get_mid(self):
        if not self.mid:
            raise IndexError('get_mid from empty stack')
        return self.mid.val

    def del_mid(self):
        if not self.mid:
            raise IndexError('del_mid from empty stack')
        node = self.mid
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.prev
        self.size -= 1

        # Вот это ключевая часть логики: после удаления из [1,2,3]:
        # останется [1,3], mid должен стать 3 (right middle)
        if self.size == 0:
            self.mid = None
        elif self.size % 2 == 0:
            self.mid = node.next
        else:
            self.mid = node.prev


stack = MidStack()
stack.push(1)  # [1]
stack.push(2)  # [1, 2]
stack.push(3)  # [1, 2, 3]
print(stack.get_mid())  # 2
stack.del_mid()  # [1, 3]
print(stack.get_mid())  # 3
