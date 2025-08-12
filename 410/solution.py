from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # we want to minimize the difference between each subarray
        
        def check(target):
            # our first chunk starts with a chunk sum of 0.
            # if k == 1, we will only have one chunk.
            # as such, start our count from 1
            count = 1
            csum = 0
            
            for n in nums:
                if csum + n > target:
                    # if we add any more, we go past our limit target
                    # increment count and reset our chunk sum
                    count += 1
                    csum = n
                else:
                    csum += n
            
            # if we make too many splits, 
            # we can increase our target sum
            # to decrease the number of splits made
            return count <= k
        
        left = max(nums) # minimum sum of one package (k = len(nums))
        right = sum(nums) # maximum sum of all packages (k = 1)
        
        while left <= right:
            mid = (left + right) // 2
            
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
                
        return left

sol = Solution() 
