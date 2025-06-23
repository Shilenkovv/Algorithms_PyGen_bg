def year_with_max_living_people(years_of_life: list[tuple[int, int]]) -> int:
    counts = [0] * 102
    for s, e in years_of_life:
        counts[s - 1800] += 1
        counts[e - 1800 + 1] -= 1
    max_living = -float('inf')
    tot_living = 0

    for i in range(len(counts)):
        if counts[i]:
            tot_living += counts[i]
            if tot_living > max_living:
                max_living = tot_living
                nice_year = 1800 + i
    return nice_year


# print(year_with_max_living_people([(1800, 1850), (1820, 1860), (1840, 1900)]))  # 1840
# print(year_with_max_living_people([(1800, 1900), (1800, 1900), (1800, 1900)]))  # 1800
# print(year_with_max_living_people([(1810, 1890)]))
