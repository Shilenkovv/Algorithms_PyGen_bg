def sort_grades(grades: list[str]) -> None:
    n = len(grades)
    grades_all = [
        'F-',
        'F',
        'F+',
        'D-',
        'D',
        'D+',
        'C-',
        'C',
        'C+',
        'B-',
        'B',
        'B+',
        'A-',
        'A',
        'A+',
    ]

    for i in range(n - 1):
        idx = i

        for j in range(i + 1, n):
            if grades_all.index(grades[j]) > grades_all.index(grades[idx]):
                idx = j
        if i != idx:
            grades[i], grades[idx] = grades[idx], grades[i]


# grades = ['B', 'C', 'A', 'F', 'A', 'D']
# sort_grades(grades)
# print(grades)  # ['A', 'A', 'B', 'C', 'D', 'F']
