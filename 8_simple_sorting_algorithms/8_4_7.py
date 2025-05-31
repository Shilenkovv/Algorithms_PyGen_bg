from collections import defaultdict


def count_pairs(nums: list[int]) -> int:
    dct = defaultdict(int)
    for i in range(len(nums)):
        dct[nums[i]] += 1

    ans = 0
    for k in dct:
        ans += ((1 + dct.get(k)) * dct.get(k)) // 2
    return ans


# print(count_pairs([-1, -2, -1, -2]))
