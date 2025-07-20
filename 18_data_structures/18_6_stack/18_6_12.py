from typing import List


def operating_time(n: int, logs: List[str]) -> List[int]:
    res: List[int] = [0] * n
    stack: List[int] = []
    prev_time = 0

    for log in logs:
        fn_id, typ, t_s = log.split(':')
        fn_id = int(fn_id)
        t = int(t_s)

        if typ == 'start':
            if stack:
                # текущая функция (на вершине стека) работала с prev_time до t-1
                res[stack[-1]] += t - prev_time
            stack.append(fn_id)
            prev_time = t
        else:  # end
            # функция на вершине работала с prev_time до t (включительно)
            res[stack.pop()] += t - prev_time + 1
            prev_time = t + 1

    return res


print(operating_time(2, ['0:start:0', '1:start:2', '1:end:5', '0:end:6']))  # [3, 4]
