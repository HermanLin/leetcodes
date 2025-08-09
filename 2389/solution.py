from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def binarySearch(target):
            left = 0
            # right = N - 1
            right = N
            
            while left < right:
                mid = (left + right) // 2
                psum = prefix_sums[mid]
                
                if psum > target:
                    right = mid
                else:
                    left = mid + 1
                    
            # if left == N - 1 and prefix_sums[left] <= target:
            #     return left + 1
            return left
        
        N = len(nums)
        nums.sort()
        
        prefix_sums = [nums[0]]
        for i in range(1, N):
            prefix_sums.append(prefix_sums[-1] + nums[i])
            
        ans = []
        for q in queries:
            i = binarySearch(q)
            ans.append(i)
            
        return ans
        

sol = Solution() 
