def expanded_form(n: int) -> str:
    if n == 0:
        return '0'
    from math import floor, log10

    digits = [0] * (floor(log10(n)) + 1)
    idx = len(digits) - 1
    while n > 0:
        digits[idx] = n % 10
        idx -= 1
        n //= 10

    ans = []
    for i, elem in enumerate(digits):
        if len(digits) - 1 - i > 1:
            ans.append(f'{elem}*10^{len(digits) - 1 - i}')
        elif len(digits) - 1 - i == 1:
            ans.append(f'{elem}*10')
        else:
            ans.append(f'{elem}')
    return ' + '.join(ans)


print(expanded_form(2854))  # 3*10^2 + 4*10 + 2
