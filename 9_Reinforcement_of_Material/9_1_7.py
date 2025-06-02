def max_sum_of_products(nums1: list[int], nums2: list[int]) -> int:
    nums1.sort(reverse=True)
    nums2.sort(reverse=True)
    tot_sum = 0

    for i in range(len(nums1)):
        tot_sum += nums1[i] * nums2[i]

    return tot_sum


# print(max_sum_of_products([2, 6, 4], [3, 1, 5]))
