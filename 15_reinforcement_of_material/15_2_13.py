from typing import List


def extra_nums(nums: List[int]):
    # XOR всех чисел
    xor_all = 0
    for num in nums:
        xor_all ^= num

    # Найдем бит, по которому x и y отличаются (самый правый установленный бит)
    diff_bit = xor_all & (-xor_all)

    x = 0
    y = 0

    # Разделим числа на две группы и вычислим XOR в каждой
    for num in nums:
        if num & diff_bit:
            x ^= num
        else:
            y ^= num

    return (x, y)
