from typing import List

def majorityElement(nums: List[int]) -> int:
    result_num, count = 0, 0
    for num in nums:
        if num == result_num:
            count += 1
        else:
            if count == 0:
                result_num = num
                count += 1
            else:
                count -= 1
    return result_num
