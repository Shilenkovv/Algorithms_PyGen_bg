def count_divisible_pairs(nums: list[int]) -> int:
    """
    Counts the number of pairs (i, j) in the list where the product of elements is divisible by 13.

    Args:
        nums (list[int]): A list of integers, where 1 <= len(nums) <= 10^5.

    Returns:
        int: The total number of pairs where its product is divisible by 13.
    """
    divided_by_13 = 0
    tot_pairs = 0
    for i in range(len(nums)):
        if not nums[i] % 13:
            tot_pairs += len(nums) - 1 - divided_by_13
            divided_by_13 += 1
    return tot_pairs
