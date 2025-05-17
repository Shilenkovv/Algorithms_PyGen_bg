def can_nest(nums1: list[int], nums2: list[int]) -> bool:
    """
    Check if one list can nest inside the other.

    Args:
        nums1 (list[int]): First list of integers.
        nums2 (list[int]): Second list of integers.

    Returns:
        bool: True if one list can nest inside the other, False otherwise.
    """
    return (
        min(nums1) > min(nums2)
        and max(nums1) < max(nums2)
        or min(nums2) > min(nums1)
        and max(nums2) < max(nums1)
    )
