def avg_values(nums: list) -> list:
    """Calculate the average of the first i elements in a list.

    Args:
        nums (list): Given list if integers, where 0 <= len(nums) <= 10^3.
        if len(nums) == 0, return an empty list.

    Returns:
        list: List of averages of the first i elements in nums.
    """
    if not nums:
        return []
    return [sum(nums[:i]) / len(nums[:i]) for i in range(1, len(nums) + 1)]
