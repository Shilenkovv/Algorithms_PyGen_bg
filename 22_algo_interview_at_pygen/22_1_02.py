from collections import deque


class Shelter:
    def __init__(self):
        self.cats: deque[str] = deque()
        self.dogs: deque[str] = deque()

    def add_cat(self, name: str):
        self.cats.append(name)

    def add_dog(self, name: str):
        self.dogs.append(name)

    def get_cat(self) -> str:
        return self.cats.popleft()

    def get_dog(self) -> str:
        return self.dogs.popleft()


# shelter = Shelter()
# shelter.add_dog('Rex')
# shelter.add_dog('Tode')
# shelter.add_dog('Ben')
# print(shelter.get_dog()) # Rox
# print(shelter.get_dog()) # Tode
# print(shelter.get_dog()) # Ben
