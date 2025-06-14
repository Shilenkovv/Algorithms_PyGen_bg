def merge_sorted_lists(nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
    result = []
    i, j, k = 0, 0, 0

    while i < len(nums1) and j < len(nums2) and k < len(nums3):
        min_value = min(nums1[i], nums2[j], nums3[k])
        if nums1[i] == min_value:
            result.append(nums1[i])
            i += 1
        elif nums2[j] == min_value:
            result.append(nums2[j])
            j += 1
        else:
            result.append(nums3[k])
            k += 1
    if i == len(nums1):
        while j < len(nums2) and k < len(nums3):
            min_value = min(nums2[j], nums3[k])
            if nums2[j] == min_value:
                result.append(nums2[j])
                j += 1
            else:
                result.append(nums3[k])
                k += 1
        while j < len(nums2):
            result.append(nums2[j])
            j += 1
        while k < len(nums3):
            result.append(nums3[k])
            k += 1
    elif j == len(nums2):
        while i < len(nums1) and k < len(nums3):
            min_value = min(nums1[i], nums3[k])
            if nums1[i] == min_value:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums3[k])
                k += 1
        while i < len(nums1):
            result.append(nums1[i])
            i += 1
        while k < len(nums3):
            result.append(nums3[k])
            k += 1
    else:
        while i < len(nums1) and j < len(nums2):
            min_value = min(nums1[i], nums2[j])
            if nums1[i] == min_value:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        while i < len(nums1):
            result.append(nums1[i])
            i += 1
        while j < len(nums2):
            result.append(nums2[j])
            j += 1

    return result


# print(merge_sorted_lists([1, 4, 6], [2, 4, 7], [2, 3, 5, 6]))
# print(merge_sorted_lists([1], [3], [2]))
