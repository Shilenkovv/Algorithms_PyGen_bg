def hex_digit(n: int) -> str:
    hex_list = ['A', 'B', 'C', 'D', 'E', 'F']

    if n <= 9:
        return str(n)
    else:
        return hex_list[n - 10]


print(hex_digit(0))  # 0
print(hex_digit(9))  # 9
print(hex_digit(15))  # F
print(hex_digit(10))  # A
