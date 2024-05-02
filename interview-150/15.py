from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = num + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result

        # solution 2
        # nums_dict = {}
        # result = set()
        
        # for i, num in enumerate(nums):
        #     nums_dict[num] = i
        
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         potential_value = -(nums[i] + nums[j])
        #         if potential_value in nums_dict and nums_dict[potential_value] != i and nums_dict[potential_value] !=j:
        #             result.add(tuple(sorted([nums[i], nums[j], potential_value])))
        # return result