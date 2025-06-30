from typing import List


def longest_ones_with_one_flip(num: int) -> int:
    num_binary_list: List[str] = []
    while num != 0:
        last_digit = str(num % 2)
        num_binary_list.append(last_digit)
        num //= 2

    ones_counter = 0
    zeros_counter = 0
    max_ones_counter = -float('inf')

    left = 0
    right = 0
    while right < len(num_binary_list):
        if num_binary_list[right] == '1':
            ones_counter += 1
        else:
            zeros_counter += 1
        if zeros_counter == 2:
            max_ones_counter = max(ones_counter + 1, max_ones_counter)
            while zeros_counter > 1:
                left += 1
                if num_binary_list[left - 1] == '0':
                    zeros_counter -= 1
                else:
                    ones_counter -= 1
        right += 1
    max_ones_counter = (
        max(ones_counter + 1, max_ones_counter)
        if zeros_counter == 1
        else max(ones_counter, max_ones_counter)
    )

    return max_ones_counter


# print(longest_ones_with_one_flip(0b11001))  # 3
# print(longest_ones_with_one_flip(0b1011011)) # 5
