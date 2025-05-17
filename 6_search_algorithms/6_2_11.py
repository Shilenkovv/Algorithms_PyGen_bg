from collections import Counter


def find_majority_element(nums: list[int]) -> int:
    """
    Finds the majority element in a list, which is an element that appears more than half the time.

    Args:
        nums (list): A list of integers, where 1 <= len(nums) <= 10^5.

    Returns:
        int: The majority element if it exists, otherwise -1.
    """
    dct = Counter(nums)
    for k, v in dct.items():
        if v > len(nums) // 2:
            return k
    return -1
