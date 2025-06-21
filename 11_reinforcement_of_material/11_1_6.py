def square_and_sort(nums: list[int]) -> list[int]:
    return sorted(map(lambda x: abs(x) ** 2, nums))
