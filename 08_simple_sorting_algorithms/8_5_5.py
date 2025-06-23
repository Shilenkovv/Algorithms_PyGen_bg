def count_holey_in_single_num(n: int):
    dct = {num: 0 for num in range(10)}
    dct.update({0: 1, 6: 1, 8: 2, 9: 1})
    holeys = 0
    divisor = 10

    n = abs(n)
    if n == 0:
        return 1
    while n != 0:
        dig = n % divisor
        holeys += dct.get(dig)
        n = n // divisor
    return holeys


def holey_sort(nums: list[int]) -> None:
    nums.sort(key=lambda x: (count_holey_in_single_num(x), x))
    # nums.sort(key=lambda x: (-len(str(abs(x))), x))


# nums = [-8, 0, -9, -6]
# holey_sort(nums)
# print(nums)
