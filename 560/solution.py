from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # use prefix sums to track the sums of subarrays given `nums`.
        # use a map to track how many times a sum is present in nums
        # given that a sum can be represented by a prefix sum as well
        # as a difference in prefix sums.
        counts = defaultdict(int)

        # initialize counts with a zero sum since the prefix sum for
        # an empty subarray is 0
        counts[0] = 1

        curr = 0 # represent the current prefix sum
        ans = 0
        for n in nums:
            curr += n
            ans += counts[curr - k]
            counts[curr] += 1

        return ans
    
sol = Solution()
print(sol.subarraySum([1,1,1], 2))
print(sol.subarraySum([1,2,3], 3))
print(sol.subarraySum([0,1,2,3,4,5], 5))
print(sol.subarraySum([1,2,1,2,1], 3))
