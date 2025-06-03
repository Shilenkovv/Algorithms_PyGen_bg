def product_in_segments(nums: list[int], segments: list[tuple[int, int]]) -> list[int]:
    prefix_mul = [1] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix_mul[i + 1] = prefix_mul[i] * nums[i]

    ans = []
    for s, e in segments:
        ans.append(prefix_mul[e + 1] // prefix_mul[s])
    return ans


# print(product_in_segments([1, 1, 5, 3, 2], [(0, 4), (3, 4)]))  # [30, 6]
# print(product_in_segments([2, 6, 1, 4, 2], [(0, 2), (1, 4)]))  # [12, 48]
# print(product_in_segments([1], [(0, 0)]))  # [1]
