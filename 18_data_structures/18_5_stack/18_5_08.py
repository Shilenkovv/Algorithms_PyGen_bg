def max_depth(exp: str) -> int:
    cnt = 0
    max_cnt = 0
    for elem in exp:
        if elem == '(':
            cnt += 1
        elif elem == ')':
            cnt -= 1
        max_cnt = max(max_cnt, cnt)
    return max_cnt


print(max_depth('(1+2)+(3+4)'))  # 1
print(max_depth('((1+2)*(3+4))'))  # 2
