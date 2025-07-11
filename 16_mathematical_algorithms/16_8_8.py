from typing import List, Tuple


def all_arithmetic_triplets(nums: List[int]) -> List[Tuple[int, int, int]]:
    nums_set = set(nums)
    ans: List[Tuple[int, int, int]] = []
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            d = nums[j] - nums[i]
            if nums[j] + d in nums_set:
                ans.append((nums[i], nums[j], nums[j] + d))

    return ans


# print(all_arithmetic_triplets([1, 2, 3, 4, 5]))
# print(all_arithmetic_triplets([1, 2, 5]))
# print(all_arithmetic_triplets([2, 4, 6]))
