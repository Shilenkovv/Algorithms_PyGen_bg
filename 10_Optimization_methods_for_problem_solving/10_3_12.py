def min_original_size(num: str) -> str:
    left, right = 0, len(num) - 1
    while left <= right:
        if any(
            [
                num[left] == '0' and num[right] == '1',
                num[left] == '1' and num[right] == '0',
            ]
        ):
            left += 1
            right -= 1
        else:
            break
    return right - left + 1


# print(min_original_size('0110101'))  # 101
# print(min_original_size('0111001'))  # 1
# print(min_original_size('101010101010101010101010101010'))
