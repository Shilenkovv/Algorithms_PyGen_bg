from typing import Optional


class Node:
    def __init__(self, value: str, next: Optional['Node'] = None, prev: Optional['Node'] = None):
        self.value = value
        self.next = next
        self.prev = prev

    def __repr__(self):
        return str(self.value)


class OneTabBrowser:
    def __init__(self, homepage: str):
        self.current = Node(homepage)

    def __repr__(self):
        return str(self.current)

    def visit(self, url: str):
        self.current.next = Node(url, next=None, prev=self.current)
        self.current = self.current.next

    def back(self, steps: int) -> str:
        n = 0
        while n < steps and self.current.prev:
            self.current = self.current.prev
            n += 1
        return self.current.value

    def forward(self, steps: int) -> str:
        n = 0
        while n < steps and self.current.next:
            self.current = self.current.next
            n += 1
        return self.current.value


browser = OneTabBrowser('beegeek.com')
browser.visit('stepik.org')
browser.visit('google.com')
print(browser.back(1))  # stepik.org
browser.visit('leetcode.com')
print(browser.back(1))  # stepik.org
print(browser.forward(1))  # leetcode.com
