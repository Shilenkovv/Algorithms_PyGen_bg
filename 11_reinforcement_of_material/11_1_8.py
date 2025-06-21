def segments_intersection(
    segments1: list[tuple[int, int]],
    segments2: list[tuple[int, int]],
) -> list[tuple[int, int]]:
    p1, p2 = 0, 0
    ans = []
    while p1 < len(segments1) and p2 < len(segments2):
        if (
            segments2[p2][0] <= segments1[p1][1] <= segments2[p2][1]
            or segments1[p1][0] <= segments2[p2][1] <= segments1[p1][1]
        ):
            ans.append(
                (max(segments1[p1][0], segments2[p2][0]), min(segments1[p1][1], segments2[p2][1]))
            )
            if segments1[p1][1] > segments2[p2][1]:
                p2 += 1
            else:
                p1 += 1
        elif segments1[p1][0] > segments2[p2][1]:
            p2 += 1
        else:
            p1 += 1

    return ans


# # print(sort_by_equation([-1, 0, 1, 2], -1, 2, -1)) # [-4, -1, -1, 0]
# print(
#     segments_intersection([(0, 3), (5, 9), (10, 11)], [(2, 4), (7, 10)])
# )  # [(2, 3), (7, 9), (10, 10)]
