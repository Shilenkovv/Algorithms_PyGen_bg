def max_digits_sum(nums: list[int]) -> int:
    cur_num = -float('inf')
    max_digits_sum = -float('inf')
    for num in nums:
        cur_digits_sum = 0
        for digit in str(num):
            if digit.isdigit():
                cur_digits_sum += int(digit)
        if cur_digits_sum >= max_digits_sum:
            if cur_digits_sum == max_digits_sum:
                cur_num = max(num, cur_num)
            else:
                max_digits_sum = cur_digits_sum
                cur_num = num
    return cur_num


# assert max_digits_sum([10, 15, 22, 27, 14, 25]) == 27
# assert max_digits_sum([10, 15, 1, 51, 6, 11]) == 51
# assert max_digits_sum([50, 0, 14, -2, 22, 41]) == 50
# assert max_digits_sum([-11]) == -11
# assert max_digits_sum([-10, 10]) == 10
