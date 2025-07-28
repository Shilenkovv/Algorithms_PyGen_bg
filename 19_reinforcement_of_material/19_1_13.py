from collections import deque
from typing import List, Tuple


def count_removed(nums: List[int]) -> int:
    stack: deque[Tuple[int, int]] = deque()
    total, left, right = 0, 0, 1
    n = len(nums)

    while right <= n:
        current_num = nums[left]

        while right < n and nums[right] == current_num:
            right += 1

        current_count = right - left

        if stack:
            last_num, last_count = stack[-1]
            if last_num == current_num:
                current_count += last_count
                stack.pop()

        if current_count >= 3:
            total += current_count
        else:
            stack.append((current_num, current_count))

        left, right = right, right + 1

    return total


# print(count_removed([1, 2, 2, 2, 3]))  # 3
# print(count_removed([1, 1, 2, 2, 2, 1, 1, 3]))  # 7
# print(count_removed([9, 9, 9, 1, 2, 3]))
