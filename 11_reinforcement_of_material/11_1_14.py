from typing import List


def count_increasing_triplets(nums: List[int]) -> int:
    ans = 0
    for i in range(1, len(nums) - 1):
        left = 0
        right = i + 1
        cur_less = 0
        cur_higher = 0
        while left < i:
            if nums[left] < nums[i]:
                cur_less += 1
            left += 1
        while right < len(nums) and cur_less > 0:
            if nums[right] > nums[i]:
                cur_higher += 1
            right += 1
        ans += cur_less * cur_higher
    return ans


# print(count_increasing_triplets([1, 0, 3, 2, 4]))  # (1, 3, 4); (1, 2, 4); (0, 3, 4); (0, 2, 4) # 4
