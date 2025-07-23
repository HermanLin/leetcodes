from typing import List
from collections import deque

class Solution: 
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)

        # monotonic queue
        queue = deque()
        ans = []

        # sliding window implementation
        for i in range(N):
            # maintain monotonic decreasing.
            # all elements in the deque smaller than the current one
            # have no chance of being the maximum, so get rid of them
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

            queue.append(i)

            # queue[0] is the index of the maximum element.
            # if queue[0] + k == i, then it is outside the window
            if queue[0] + k == i:
                queue.popleft()
            
            # only add to the answer once our window has reached size k
            if i >= k - 1:
                ans.append(nums[queue[0]])

        return ans
    
sol = Solution() 
print(sol.maxSlidingWindow([1,3,2,-3,1,3,6,7], 3))
print(sol.maxSlidingWindow([10,9,8,7,6,5,20], 3))
