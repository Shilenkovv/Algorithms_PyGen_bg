def could_type(word: str, typed: str) -> bool:
    left, right = 0, 0

    while left < len(word):
        found = False
        while right < len(typed) and word[left] == typed[right]:
            right += 1
            found = True
            if left < len(word) - 1 and word[left] == word[left + 1]:
                break
        left += 1
        if not found:
            return False
    return left == len(word) and right == len(typed)


# print(could_type('python', 'pyytttthonnn'))  # True
# print(could_type('beegeek', 'geekbee'))  # False
# print(could_type('hello', 'helo'))
# print(could_type('aa', 'aa'))  # True
