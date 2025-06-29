def max_binary_gap(num: int) -> int:
    num_binary = bin(num).replace('0b', '')

    left = 0
    max_breach = 0
    cur_breach = 0

    while left < len(num_binary):
        if num_binary[left] == '1':
            max_breach = max(max_breach, cur_breach)
            cur_breach = 0
        else:
            cur_breach += 1
        left += 1
    return max_breach


print(max_binary_gap(44))  # 44 = 101100₂ # 1
print(max_binary_gap(32))  # 32 = 100000₂ # 0
print(max_binary_gap(69))  # 69 = 1000101₂ # 3
