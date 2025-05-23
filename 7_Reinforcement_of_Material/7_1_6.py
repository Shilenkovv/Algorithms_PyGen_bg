def count_triplets(n: int) -> int:
    tot_triplets = 0
    for i in range(1, n + 1):
        if i * (n // i) == n:
            tot_triplets += (n // i) - 1
        elif i * (n // i) < n:
            tot_triplets += n // i
    return tot_triplets


# print(count_triplets(3))  # 3
# print(count_triplets(1))  # 0
# print(count_triplets(5))  # 8
# print(count_triplets(10))  # 23
