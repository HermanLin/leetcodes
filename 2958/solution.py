from collections import defaultdict
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)

        max_len = 0
        left = 0
        for right in range(len(nums)):
            counts[nums[right]] += 1

            while counts[nums[right]] > k:
                counts[nums[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

sol = Solution() 
