def find_num(nums: list[int]) -> int:
    nums.sort()
    a, b, x1, x2, _, _, _, cd = nums

    if a * b == x1:
        return cd // x2

    return cd // x1


# print(find_num([2, 3, 4, 1, 12, 6, 2, 4]))  # 4
# print(find_num([2, 6, 7, 3, 14, 35, 15, 5]))  # 7
# print(find_num([54, 979, 242, 22, 11, 89, 1188, 4806]))  # 89
# print(find_num([1, 10, 2, 10, 6, 3, 30, 2]))
