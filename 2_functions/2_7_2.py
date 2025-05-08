def polynomial(p: tuple) -> str:
    ans = ''
    first_done = False
    for i, elem in enumerate(p):
        if not first_done:
            if elem == 0:
                continue
            elif elem == -1:
                ans += '-'
                if i == len(p) - 1:
                    ans += f'{abs(elem)}'
            elif elem == +1:
                if i == len(p) - 1:
                    ans += f'{abs(elem)}'
            elif elem != 1:
                ans += f'{elem}'
            if len(p) - i - 1 == 1:
                ans += 'x'
            elif len(p) - i - 1 > 1:
                ans += f'x^{len(p) - i - 1}'
            first_done = True
        else:
            if elem != 0:
                if elem == 1:
                    ans += '+'
                    if i == len(p) - 1:
                        ans += f'{elem}'
                elif elem == -1:
                    ans += '-'
                    if i == len(p) - 1:
                        ans += f'{abs(elem)}'
                elif elem < 0:
                    ans += f'-{abs(elem)}'
                elif elem > 0:
                    ans += f'+{elem}'
                if len(p) - i - 1 == 1:
                    ans += 'x'
                elif len(p) - i - 1 > 1:
                    ans += f'x^{len(p) - i - 1}'

    return ans
