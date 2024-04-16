from typing import List

def removeElement(nums: List[int], val: int) -> int:
        pointer = 0
        for idx, num in enumerate(nums):
            if num != val:
                nums[pointer] = num
                pointer += 1
        return pointer

