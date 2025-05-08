def equilibrium(nums: list) -> int:
    """
    Finds the index of an equilibrium point in a list of integers.

    An equilibrium point is an index where the sum of elements to the left
    of the index is equal to the sum of elements to the right of the index.
    If there are multiple equilibrium points, the function returns the first one.
    If no such index exists, the function returns -1.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The index of the equilibrium point, or -1 if no such point exists.

    Examples:
        >>> equilibrium([1, 7, 3, 6, 5, 6])
        3
        >>> equilibrium([1, 2, 3])
        -1
        >>> equilibrium([2, -2, 0])
        2
    """
    if sum(nums[:-1]) == 0 and not all([map(lambda x: x == 0, nums)]):
        return len(nums) - 1
    pre_sum = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        pre_sum[i] = nums[i - 1] + pre_sum[i - 1]
    for i in range(1, len(pre_sum)):
        if pre_sum[i - 1] == pre_sum[-1] - pre_sum[i]:
            return i - 1
    return -1
