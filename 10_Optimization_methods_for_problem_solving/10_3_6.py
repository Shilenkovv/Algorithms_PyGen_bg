def card_game_results(nums: list[int]) -> tuple[int, int]:
    ans = [0, 0]
    left, right = 0, len(nums) - 1
    turn = 0
    while left <= right:
        if nums[left] < nums[right]:
            ans[turn % 2] += nums[right]
            right -= 1
        else:
            ans[turn % 2] += nums[left]
            left += 1
        turn += 1

    return tuple(ans)


# print(card_game_results([3, 5, 1, 4, 2]))  # (6, 9)
# print(card_game_results([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))  # (30, 25)
# print(card_game_results([6, 2, 1, 5, 3, 4])) # (11, 10)
