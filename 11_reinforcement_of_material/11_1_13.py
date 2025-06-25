def count_ways_to_form(s1: str, s2: str) -> int:
    prefix_first_s = [0] * (len(s1) + 1)
    prefix_third_s = [0] * (len(s1) + 1)

    for i in range(1, len(prefix_first_s)):
        prefix_first_s[i] = prefix_first_s[i - 1] + (s1[i - 1] == s2[0])
        prefix_third_s[i] = prefix_third_s[i - 1] + (s1[i - 1] == s2[2])

    ans = 0
    for i in range(1, len(s1)):
        if s1[i] == s2[1]:
            ans += (prefix_first_s[i] - prefix_first_s[0]) * (
                prefix_third_s[len(prefix_third_s) - 1] - prefix_third_s[i + 1]
            )
    return ans


# print(count_ways_to_form('bebebsi', 'beb')) # 4
print(count_ways_to_form('beegeek', 'top'))  # 0
print(count_ways_to_form('a', 'aaa'))  # 0
print(count_ways_to_form('bee', 'bee'))  # 1
print(count_ways_to_form('aaaaa', 'aaa'))  # 10
print(count_ways_to_form('abc', 'cba'))  # 0
