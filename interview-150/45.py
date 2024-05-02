from typing import List

def jump(nums: List[int]) -> int:
    count = l = r = 0
    while r < len(nums) - 1:
        max_idx = 0
        for i in range(l, r+1):
            max_idx = max(max_idx, i+nums[i])
        l = r + 1
        r = max_idx
        count += 1
    return count