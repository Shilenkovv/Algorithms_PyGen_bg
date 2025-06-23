from collections import Counter


def max_possible_number(nums1: list[int], nums2: list[int]) -> int:
    cnt1 = Counter(nums1)
    cnt2 = Counter(nums2)

    ans_str = ''
    for digit in sorted(cnt1, reverse=True):
        if digit in cnt2:
            ans_str += str(digit) * min(cnt1.get(digit), cnt2.get(digit))

    return int(ans_str) if ans_str else -1


# print(max_possible_number([8, 1, 0, 8], [1, 0, 8, 8, 7]))
