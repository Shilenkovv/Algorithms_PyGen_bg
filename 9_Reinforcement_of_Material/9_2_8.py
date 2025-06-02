def common_free_time(plan: list[tuple[int, int]]) -> int:
    counts = [0] * 25
    for empl in plan:
        for s, e in empl:
            counts[s] += 1
            counts[e] -= 1
    tot_working = 0

    fun = []
    s_fun = float('inf')
    for i in range(len(counts)):
        tot_working += counts[i]
        if tot_working == 0:
            if s_fun == float('inf'):
                s_fun = i
        elif tot_working > 0 and s_fun != float('inf'):
            fun.append((s_fun, i))
            s_fun = float('inf')
    if s_fun != float('inf') and s_fun != 23:
        fun.append((s_fun, 23))
    return fun


# print(common_free_time([[(1, 2), (3, 4)], [(5, 6), (7, 8)]]))
# print(common_free_time([[(1, 2)]]))
