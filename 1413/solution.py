from typing import List

'''
[-3,2,-3,4,2]
=> -3, -1, -4, 0, 2

[1,-2,-3]
=> 1, -1, -4
'''

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        '''
        N = len(nums)
        
        # use prefix sums to track the sum at each step
        prefix_sums = [nums[0]]
        for i in range(1, N):
            prefix_sums.append(nums[i] + prefix_sums[-1])
            
        # ...then determine which step has the minimum sum
        curr = 0
        for i in range(N):
            if prefix_sums[i] < curr:
                curr = prefix_sums[i]
               
        if curr <= 0:
            return abs(curr) + 1
        return curr
        '''

        # improved solution
        # disregard the array and track the minimum as we loop
        '''
        N = len(nums)

        curr = total = 0
        for i in range(N):
            total += nums[i]
            if total < curr:
                curr = total

        if curr <= 0:
            return abs(curr) + 1
        return curr
        '''

        # optimized solution
        # the same as above, using more pythonic approach
        minimum = total = 0
        
        for n in nums:
            total += n
            minimum = min(minimum, total)

        return 1 - minimum