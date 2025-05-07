def even_odd(nums: list) -> bool:
    """Returns True if all even numbers are at the beginning of the list and all odd numbers are at the end of the list.
    If the list is has only one element, it returns True.

    Args:
        nums (list): Given list of integers, where 1 <= len(nums) <= 10^3

    Returns:
        bool: True if all numbers are even or all numbers are odd, False otherwise.
    """
    if len(nums) == 1:
        return True
    first_is_even = nums[0] % 2 == 0
    for i in range(1, len(nums)):
        if nums[i] % 2 == 0 and not first_is_even:
            return False
        elif nums[i] % 2 == 1 and first_is_even:
            return False
    return True
