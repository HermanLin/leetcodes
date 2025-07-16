from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # if we treat 0s as -1s, we can try to find
        # the longest subarray with the sum 0 since
        # a sum of 0 will guarantee equal number of
        # 0s and 1s
        
        # prefix_map = {} # synonymous to a cache
        cache = {}
        longest = 0
        prefix_sum = 0

        N = len(nums)
        for i in range(N):
            # n = 1 if nums[i] else -1
            # prefix_sum += n
            prefix_sum += (1 if nums[i] else -1)

            if prefix_sum == 0:
                longest = i + 1
            elif prefix_sum in cache:
               # usually, you would check for prefix_sum - k in cache,
               # but we're trying to find a k of 0
               longest = max(longest, i - cache[prefix_sum])
            else:
                # track the lowest index of when this sum appears
                cache[prefix_sum] = i

        return longest
    
sol = Solution()
print(sol.findMaxLength([0,1]))
print(sol.findMaxLength([0,1,0])) 
print(sol.findMaxLength([0,1,1,1,1,1,0,0,0]))
print(sol.findMaxLength([0, 1, 1, 1, 1, 1, 0, 1, 0, 1]))
print(sol.findMaxLength([1, 1, 0, 0, 1, 1, 0, 1, 0, 1]))
print(sol.findMaxLength([0, 0, 0, 1, 1, 0, 0, 1, 1, 0]))
print(sol.findMaxLength([1, 0, 1, 1, 0, 1, 1, 1, 0, 1]))
print(sol.findMaxLength([0, 0, 0, 1, 1, 0, 1, 1, 1, 1]))
print(sol.findMaxLength([1, 0, 0, 0, 1, 1, 0, 1, 1, 0]))
print(sol.findMaxLength([0, 0, 1, 0, 0, 1, 1, 1, 0, 1]))
print(sol.findMaxLength([0, 1, 0, 1, 0, 0, 1, 0, 0, 0]))
print(sol.findMaxLength([1, 1, 1, 1, 1, 1, 1, 1]))