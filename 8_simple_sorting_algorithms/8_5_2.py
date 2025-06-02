def max_sum_of_k_elements(nums: list[int], k: int) -> int:
    nums.sort()
    return sum(nums[-k:])


# print(find_triple([8, 5, 7, 4]))
