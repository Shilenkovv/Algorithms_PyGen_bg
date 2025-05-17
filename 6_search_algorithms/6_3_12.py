def find_index_of_max(nums: list[int], reverse: bool = False) -> int:
    cur_max = -float('inf')
    indx = []
    for i, num in enumerate(nums):
        if num > cur_max:
            cur_max = num
            indx = [i]
        elif num == cur_max:
            indx.append(i)
    return indx[-1] if reverse else indx[0]


assert find_index_of_max([1, 5, 3, 2, 4]) == 1
assert find_index_of_max([3, 2, 4, 1, 4]) == 2
assert find_index_of_max([3, 2, 4, 1, 4], reverse=True) == 4
