def sort_by_equation(nums: list[int], a: int, b: int, c: int) -> list[int]:
    return sorted([a * num**2 + b * num + c for num in nums])


# print(sort_by_equation([-1, 0, 1, 2], -1, 2, -1)) # [-4, -1, -1, 0]
