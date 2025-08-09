from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)
        
        left = 0
        right = N - 1
        
        while left <= right:
            mid = (left + right) // 2
            num = nums[mid]
            
            # if num == target:
            #     return mid
            
            if num < target:
                left = mid + 1
            # elif num > target:
            #     right = mid - 1
            else:
                right = mid
                
        return left

sol = Solution() 
print(sol.searchInsert([2, 5, 9, 13, 15, 16, 19, 22, 24, 25, 26, 34, 40, 41, 45, 46, 48, 49, 55, 57, 59, 61, 66, 67, 71, 74, 75, 77, 81, 82, 89, 90, 92, 93, 94, 95, 96, 98], 5))
print(sol.searchInsert([2, 5, 9, 13, 15, 16, 19, 22, 24, 25, 26, 34, 40, 41, 45, 46, 48, 49, 55, 57, 59, 61, 66, 67, 71, 74, 75, 77, 81, 82, 89, 90, 92, 93, 94, 95, 96, 98], 73))
