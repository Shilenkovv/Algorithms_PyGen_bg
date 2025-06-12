from collections import defaultdict


def happy_tickets(n: int) -> int:
    four_dig_sum_freq = defaultdict(int)

    for frstd in range(10):
        for sd in range(10):
            for td in range(10):
                for frthd in range(10):
                    four_dig_sum_freq[frstd + sd + td + frthd] += 1
    return four_dig_sum_freq[n] ** 2


# print(happy_tickets(1))  # 16
# print(happy_tickets(2))  # 100
# print(happy_tickets(5))  # 3136
