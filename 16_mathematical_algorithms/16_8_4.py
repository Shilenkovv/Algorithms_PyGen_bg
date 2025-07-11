from typing import List


def can_form_arithmetic(nums: List[int]) -> bool:
    n = len(nums)
    n_unique = len(set(nums))
    if n_unique == 1:
        return True
    elif n_unique != n:
        return False
    first_elem, last_elem = min(nums), max(nums)
    d = (last_elem - first_elem) / (n - 1)
    for i in range(1, n):
        if (nums[i] - nums[i - 1]) % d != 0:
            return False
    return True


# print(can_form_arithmetic([1, 1, 4, 4, 5]))  # False
# print(can_form_arithmetic([8, 0, 2, 6, 4]))  # True
# print(can_form_arithmetic([12, 9, 15, 6]))  # True
# print(can_form_arithmetic([-6, 6, -2, 2]))  # True
# print(can_form_arithmetic([2, 4, 1, 7, 3]))  # False
# print(can_form_arithmetic([1, 10]))  # True
# print(can_form_arithmetic([1, 1, 1, 1]))  # True
