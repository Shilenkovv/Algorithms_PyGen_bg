left = 0
right = 10**10 - 1
while True:
    middle = left + (right - left) // 2
    res = guess(middle + 1)
    if res == 'Отгадал!':
        print(middle + 1)
        break
    elif res == 'Меньше':
        right = middle - 1
    elif res == 'Больше':
        left = middle + 1
    else:
        raise Exception(f'{res = }')
