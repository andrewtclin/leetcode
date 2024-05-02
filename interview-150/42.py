from typing import List

def trap(height: List[int]) -> int:
    length = len(height)
    left_mins = [0] * length
    right_maxs = [0] * length
    min_height = 0
    max_height = 0

    for left in range(length):
        right = -left - 1

        left_mins[left] = min_height
        right_maxs[right] = max_height

        min_height = max(min_height, height[left])
        max_height = max(max_height, height[right])

    rain_traps = [0] * length
    for i in range(length):
        potential_trap = min(left_mins[i], right_maxs[i])
        rain_traps[i] = max(0, potential_trap - height[i])
    
    return sum(rain_traps)