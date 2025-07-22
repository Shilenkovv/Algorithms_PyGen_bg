from collections import deque
from typing import List


def moving_avg(nums: List[int], k: int) -> List[float]:
    deq: deque[int] = deque()
    tot_sum = 0
    ans: List[float] = []
    i = 0

    while i < k:
        elem = nums[i]
        tot_sum += elem
        deq.append(elem)
        i += 1

    ans.append(tot_sum / k)

    while i < len(nums):
        elem = nums[i]

        tot_sum -= deq.popleft()
        tot_sum += elem
        deq.append(elem)
        ans.append(tot_sum / k)
        i += 1
    return ans


print(moving_avg([1, 2, 3, 4, 5], 2))  # [1.5, 2.5, 3.5, 4.5]
