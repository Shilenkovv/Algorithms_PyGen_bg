left = 0
right = 1
if guess(right) == 'Отгадал':
    print(right)
while guess(right) == 'Больше':
    right *= 2

left = right // 2

while left <= right:
    middle = (left + right) // 2
    ans = guess(middle + 1)
    if ans == 'Отгадал!':
        print(middle + 1)
        break
    if ans == 'Больше':
        left = middle + 1
    else:
        right = middle - 1
