def index_of_first_occurrence(s1: str, s2: str) -> int:
    p1 = 0

    while p1 <= len(s1) - len(s2):
        if s1[p1] != s2[0]:
            p1 += 1
            continue
        for i in range(1, len(s2)):
            if s1[p1 + i] != s2[i]:
                p1 += 1
                break
        else:
            return p1
    return -1


# print(intersection_of_three_lists([1, 2, 3, 4, 5], [1, 3, 5], [3, 4, 5])) # [3, 5]
# print(intersection_of_three_lists([1, 3], [4], [7, 8, 9]))  # []
# print(intersection_of_three_lists([0, 1, 2], [-1, 0, 1], [-2, -1, 0]))  # [0]
# print(index_of_first_occurrence('beegeek', 'geek')) # 3
# print(index_of_first_occurrence('beegeek', 'beegek'))  # -1
