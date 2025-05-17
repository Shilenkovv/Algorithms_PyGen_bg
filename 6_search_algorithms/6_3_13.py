from collections import Counter


def find_number(nums: list[int]) -> int:
    dct = Counter(nums)
    max_val = -float('inf')
    for k, v in dct.items():
        if k == v:
            max_val = max(max_val, k)
    return max_val if max_val != -float('inf') else -1


# assert find_number([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4
assert find_number([2, 3, 4, 5]) == -1
