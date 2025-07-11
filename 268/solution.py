from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        # guaranteed to be missing one number, add 1 to accommodate
        N = len(nums) + 1
        checks = [False] * N

        for n in nums:
            checks[n] = True

        for i in range(N):
            if not checks[i]:
                return i
            
        return -1
        '''
    
        # improved solution, using O(1) space
        N = len(nums)
        true_sum = N * (N + 1) // 2 # triangular number formula

        '''
        for n in nums:
            true_sum -= n
        '''

        return true_sum - sum(nums)
