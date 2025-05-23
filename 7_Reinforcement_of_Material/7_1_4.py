from math import floor, log10


def count_numbers_with_equal_halves(n: int) -> int:
    ans = 0
    for i in range(10, n + 1):
        digits_cnt = floor(log10(i)) + 1
        if not digits_cnt % 2 and i // (10 ** (digits_cnt / 2)) == i % (10 ** (digits_cnt / 2)):
            ans += 1
    return ans


# print(count_numbers_with_equal_halves(50))  # 4
# print(count_numbers_with_equal_halves(10))  # 0
# print(count_numbers_with_equal_halves(1))  # 1
# print(count_numbers_with_equal_halves(5000))
# print(min_distance_between_peaks([1, 2, 3, 4, 5, 6, 7, 8]))
# print(min_distance_between_peaks([1]))
# print(min_distance_between_peaks([1, 2, 1]))
# print(min_distance_between_peaks([-1, 1, 0, 1, -1]))
