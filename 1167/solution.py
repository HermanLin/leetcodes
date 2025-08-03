import heapq
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        cost = 0
        
        while len(sticks) > 1:
            one = heapq.heappop(sticks)
            two = heapq.heappop(sticks)
            
            cost += one + two
            heapq.heappush(sticks, one + two)
            
        return cost

sol = Solution() 
