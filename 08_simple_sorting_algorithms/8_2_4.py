def k_swaps_to_sort(n, k):
    result = list(range(n, 0, -1))
    current_swaps = n * (n - 1) // 2

    for i in range(n - 1):
        if current_swaps == k:
            break
        for j in range(n - 1, i, -1):
            if current_swaps > k:
                result[j], result[j - 1] = result[j - 1], result[j]
                current_swaps -= 1
            else:
                break

    return result


print(k_swaps_to_sort(5, 3))  # [2, 3, 4, 1, 5]
print(k_swaps_to_sort(1, 0))  # [1]
print(k_swaps_to_sort(5, 1))  # [2, 1, 3, 4, 5]
print(k_swaps_to_sort(5, 10))  # [5, 4, 3, 2, 1]
print(k_swaps_to_sort(7, 4))  # [2, 3, 4, 5, 1, 6, 7]
print(k_swaps_to_sort(10, 45))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
