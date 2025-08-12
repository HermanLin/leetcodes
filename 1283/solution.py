import math
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(divisor):
            total = 0
            for n in nums:
                total += math.ceil(n / divisor)
                
            return total <= threshold
        
        left = 1
        right = max(nums)
        
        while left <= right:
            mid = (left + right) // 2
            
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
                
        return left

sol = Solution() 
