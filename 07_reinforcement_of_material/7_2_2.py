def find_number(nums):
    seen = set()
    result = 0

    for num in nums:
        if num not in seen:
            result += num
            seen.add(num)
        else:
            result -= num

    return result
