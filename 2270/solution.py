from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        '''
        N = len(nums)

        prefix_sums = [nums[0]]
        for i in range(1, N):
            # add nums[i] to the last prefix sum
            prefix_sums.append(nums[i] + prefix_sums[-1])

        ans = 0
        for i in range(N - 1):
            # calculate sums
            left_sum = prefix_sums[i]
            right_sum = prefix_sums[-1] - left_sum

            if left_sum >= right_sum:
                ans += 1

        return ans
        '''

        # improved solution with O(1) space complexity instead
        N = len(nums)
        ans = left_sum = 0
        total = sum(nums)

        for i in range(N - 1):
            # left_sum is just the sum up until i.
            # we can calculate it without a prefix sum array
            left_sum += nums[i]

            # right_sum is always the sum of entire nums minus the left
            right_sum = total - left_sum

            if left_sum >= right_sum:
                ans += 1

        return ans

sol = Solution()
print(sol.waysToSplitArray([10,4,-8,7]))
print(sol.waysToSplitArray([2,3,1,0]))
print(sol.waysToSplitArray([0,0]))
print(sol.waysToSplitArray([9,9,9]))
print(sol.waysToSplitArray([6,-1,9]))
print(sol.waysToSplitArray([0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-96,-97,-98,-99,-100]))
