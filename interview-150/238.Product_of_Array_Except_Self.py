from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    length = len(nums)
    l_list = [0] * length
    l_acc = 1
    r_list = [0] * length
    r_acc = 1

    for l in range(len(nums)):
        r = -l-1
        l_list[l] = l_acc
        r_list[r] = r_acc
        l_acc *= nums[l]
        r_acc *= nums[r]
    
    return [l*r for l, r in zip(l_list, r_list)]