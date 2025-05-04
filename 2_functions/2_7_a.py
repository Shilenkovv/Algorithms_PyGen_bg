def polynomial_sum(p1: tuple, p2: tuple) -> str:
    coefficients = [0] * max(len(p1), len(p2))
    if len(p1) == len(p2):
        max_len = len(p1)
        for i in range(len(p1)):
            coefficients[i] = p1[i] + p2[i]
    else:
        max_len = max(len(p1), len(p2))
        longer = p1
        shorter = p2
        if max_len == len(p2):
            longer, shorter = shorter, longer
        len_diff = len(longer) - len(shorter)

        for i in range(max_len):
            coefficients[i] = longer[i] + shorter[i - len_diff] if i >= len_diff else longer[i]
    first_nonzero_ind = -1
    for i in range(max_len):
        if first_nonzero_ind == -1:
            if coefficients[i] != 0:
                first_nonzero_ind = i
                break
    return tuple(coefficients[first_nonzero_ind:])

    # ans = ''
    # first_done = False
    # for i, elem in enumerate(coefficients):
    #     if not first_done:
    #         if elem == 0:
    #             continue
    #         elif elem == -1:
    #             ans += '-'
    #         elif elem != 1:
    #             ans += f'{elem}'
    #         if max_len - i - 1 == 1:
    #             ans += 'x'
    #         elif max_len - i - 1 > 1:
    #             ans += f'x^{max_len - i - 1}'
    #         first_done = True
    #     else:
    #         if elem != 0:
    #             ans += ' '
    #             if elem == 1:
    #                 ans += '+ '
    #             elif elem == -1:
    #                 ans += '- '
    #             elif elem < 0:
    #                 ans += f'- {abs(elem)}'
    #             elif elem > 0:
    #                 ans += f'+ {elem}'
    #             if max_len - i - 1 == 1:
    #                 ans += 'x'
    #             elif max_len - i - 1 > 1:
    #                 ans += f'x^{max_len - i - 1}'

    # return ans


# p1 = (1, 7, 0, -4)
# p2 = (-1, 0, 0, 2)
# print(polynomial_sum(p1, p2))


# p1 = (1, 1, 1, 1)
# p2 = (-1, -1, -1, -1, -1)
# print(polynomial_sum(p1, p2))
