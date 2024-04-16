from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if n == 0:
        return nums1
    
    nums2_pointer = n - 1
    nums1_pointer = m - 1
    merged_array_pointer = len(nums1) - 1

    while nums2_pointer >= 0:
        if nums2[nums2_pointer] >= nums1[nums1_pointer]:
            nums1[merged_array_pointer] = nums2[nums2_pointer]
            nums2_pointer -= 1
        else:
            nums1[merged_array_pointer] = nums1[nums1_pointer]
            nums1_pointer -= 1
            if nums1_pointer < 0:
                i = 0
                for element in nums2[:nums2_pointer+1]:
                    nums1[i] = element
                    i += 1
                break
        merged_array_pointer -= 1
    return nums1