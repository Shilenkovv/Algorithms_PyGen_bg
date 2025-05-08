def is_order(nums: list, strict: bool = True):
    """
    Checks if a list of numbers is sorted (in ascending or descending order).
    Optionally checks for strict ordering (no duplicates).

    Args:
        nums (list): The list of numbers to check.
        strict (bool, optional): If `True`, ensures the list is strictly ordered
                                 (no duplicate values). Defaults to `True`.

    Returns:
        bool: `True` if the list is ordered (and strictly ordered if `strict=True`),
              `False` otherwise.
    """
    if len(nums) < 2:
        return True
    if nums != sorted(nums) and nums != sorted(nums, reverse=True):
        return False
    if strict:
        if len(set(nums)) != len(nums):
            return False
    return True
