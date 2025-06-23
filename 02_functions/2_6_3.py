def quadratic(x1: int, x2: int) -> str:
    a = 1
    b = -a * (x1 + x2)
    c = a * (x1 * x2)

    ans_a = 'x^2 '
    if b == 1:
        ans_b = '+ x '
    elif b == -1:
        ans_b = '- x '
    elif b == 0:
        ans_b = ''
    elif b > 0:
        ans_b = f'+ {b}x '
    else:
        ans_b = f'- {abs(b)}x '
    if c == 0:
        ans_c = ''
    elif c > 0:
        ans_c = f'+ {c} '
    else:
        ans_c = f'- {abs(c)} '
    return ans_a + ans_b + ans_c + '= 0'
