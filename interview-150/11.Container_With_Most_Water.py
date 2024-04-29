from typing import List
def maxArea(height: List[int]) -> int:
    i = 0
    j = len(height) - 1
    max_area = 0

    while i < j:
        new_area = min(height[i], height[j]) * (j - i)
        max_area = max(max_area, new_area)

        if height[i] > height[j]:
            j -= 1
        else: i += 1
        
    return max_area