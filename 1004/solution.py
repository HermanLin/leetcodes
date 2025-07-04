from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ''' 
        N = len(nums)
        left = 0
        
        zero_count = 0
        max_len = 0
        for right in range(N):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
            
        return max_len
        '''

        # improved solution
        '''
        essentially does the same thing as above solution, but
        uses k to keep track of zeros instead. The difference
        b/w `left` and `right` inherently keeps track of the 
        maximum subarray length that contains at most k zeros
        without the need for comparisons
        '''
        N = len(nums)
        left = 0
        for right in range(N):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

        # return right - left + 1
        return N - left