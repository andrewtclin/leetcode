from typing import List

def removeDuplicates(self, nums: List[int]) -> int:
    pointer, cursor = 0, 0

    while cursor < len(nums):
        count = 1
        while cursor + 1 < len(nums) and nums[cursor] == nums[cursor + 1]:
            count += 1
            cursor += 1

        for i in range(min(2, count)):
            nums[pointer] = nums[cursor]
            pointer += 1
        
        cursor += 1
    return pointer