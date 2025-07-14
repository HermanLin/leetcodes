from typing import List
from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        '''
        # use prefix sum approach to track how many odd numbers
        # there are in a subarray up to i instead of the sum.
        # e.g.
        # [1,1,2,1,1] -> prefix count -> [1,2,2,3,4]
        #
        # any time we encounter a "sum" (count) of k, we 
        # increment our answer.
`
        counts = defaultdict(int)
        counts[0] = 1 # initialize an empty prefix count answer

        curr = ans = 0
        for n in nums:
            curr += n % 2
            ans += counts[curr - k]
            counts[curr] += 1

        return ans
        '''

        # another solution using sliding window
        N = len(nums)
        left = middle = ans = 0

        odd_count = 0
        for right in range(N):
            # keep track of how many odd numbers we encounter
            if nums[right] % 2 == 1:
                odd_count += 1

            while odd_count > k:
                # if we go past the strict limit of odd numbers...
                if nums[left] % 2 == 1:
                    odd_count -= 1  # ...find and remove an odd number
                left += 1           # ..."slide" our window
                middle = left       # ...move our subarray pointer

            if odd_count == k:
                # if we find the exact limit of odd numbers...
                while nums[middle] % 2 == 0:
                    # ...we move our subarray pointer over as many places
                    # as possible as to keep within our limit. This represents
                    # how many subarrays are still valid 
                    middle += 1
                ans += (middle - left) + 1 # ...and add that many valid to ans

        return ans

    
sol = Solution()
print(sol.numberOfSubarrays([1,1,2,1,1], 3))
print(sol.numberOfSubarrays([2,4,6], 1))
print(sol.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2))
# prefix odd counts (curr) = [0,0,0,1,1,1,2,2,2,2]







'''

left, middle, oddNums = 0, 0, 0
ans = 0
for num in nums:
    if num % 2:
        oddNums += 1
    
    
    while oddNums > k:
        if nums[left] % 2:
            oddNums -= 1
        left += 1
        middle = left
    
    if oddNums == k:
        while not nums[middle] % 2:
            middle += 1
        ans += (middle - left) + 1
    #print(left, middle, oddNums)

return ans

'''