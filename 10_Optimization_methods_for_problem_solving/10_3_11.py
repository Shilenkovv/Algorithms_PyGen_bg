def is_flippable_number(num: str) -> bool:
    left, right = 0, len(num) - 1
    while left <= right:
        if any(
            [
                num[left] == '6' and num[right] == '9',
                num[left] == '9' and num[right] == '6',
                num[left] == num[right] == '0',
            ]
        ):
            left += 1
            right -= 1
        else:
            return False
    return True


# print(is_flippable_number('609'))  # True
# print(is_flippable_number('96096'))  # True
# print(is_flippable_number('6900'))  # False
# print(is_flippable_number('6'))  # False
