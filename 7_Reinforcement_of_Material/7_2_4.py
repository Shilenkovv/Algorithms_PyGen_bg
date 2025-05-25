def smallest_missing_positive(nums: list[int]) -> int:
    seen = set()
    for elem in nums:
        if elem > 0:
            seen.add(elem)
    for i in range(1, len(nums) + 2):
        if i not in seen:
            return i
