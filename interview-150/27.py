from typing import List

def removeElement(nums: List[int], val: int) -> int:
        pointer = 0
        for i in range(len(nums)):
                if nums[i] != val:
                        nums[pointer] = nums[i]
                        pointer += 1
        return pointer

        # solution 2
        # l_ptr, r_ptr = 0, 0

        # while r_ptr < len(nums):
        #     if nums[r_ptr] != val:
        #         nums[l_ptr] = nums[r_ptr]
        #         l_ptr += 1
        #     r_ptr += 1
        # return l_ptr