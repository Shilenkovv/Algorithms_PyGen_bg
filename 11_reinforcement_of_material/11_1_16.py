def bonus_problem() -> int:
    powers = {num**5: num for num in range(1, 151)}
    for a in range(1, 148):
        print(f'a = {a}')
        for b in range(a + 1, 149):
            for c in range(b + 1, 150):
                for d in range(c + 1, 151):
                    res = a**5 + b**5 + c**5 + d**5
                    if res in powers:
                        return a + b + c + d + powers.get(res, 9999999)


print(bonus_problem())
