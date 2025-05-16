def is_possible_to_split(nums: list[int]) -> bool:
    """
    Determines if the given list of integers can be split into pairs such that
    the product of the smallest and largest numbers in each pair is the same.

    Args:
        nums (list[int]): A list of integers to be checked.

    Returns:
        bool: True if the list can be split into pairs with equal products, False otherwise.
    """
    nums = sorted(nums)
    mul = nums[0] * nums[-1]
    for i in range(1, len(nums) // 2):
        if nums[i] * nums[len(nums) - i - 1] != mul:
            return False
    return True
