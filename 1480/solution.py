from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [nums[0]]

        for i in range(1, N):
            ans.append(nums[i] + ans[-1])

        return ans