left = 1
right = int(input())

while left <= right:
    middle = left + (right - left) // 2
    if is_stable_version(middle):
        left = middle + 1
    else:
        right = middle - 1
while True:
    cur_ver = is_stable_version(left)
    prev_ver = is_stable_version(left - 1)
    if cur_ver != prev_ver and not cur_ver and prev_ver:
        print(left)
        break
    else:
        left -= 1
