def sum_multiples_of_two_or_five(k: int) -> int:
    twos = k // 2
    fives = k // 5
    tens = k // 10
    sum_of_twos = ((2 * 2 + 2 * (twos - 1)) * twos) // 2
    sum_of_fives = ((2 * 5 + (fives - 1) * 5) * fives) // 2 if fives else 0
    sum_of_tens = ((2 * 10 + (tens - 1) * 10) * tens) // 2 if tens else 0
    return sum_of_twos + sum_of_fives - sum_of_tens


# print(sum_multiples_of_two_or_five(5))  # 11
# print(sum_multiples_of_two_or_five(15))  # 76
# print(sum_multiples_of_two_or_five(25))  # 201
# print(sum_multiples_of_two_or_five(10))  2 4 6 8 10   5 10    10
