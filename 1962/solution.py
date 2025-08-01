import heapq
import math
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        '''N = len(piles)
        maxHeap = [-p for p in piles]
        heapq.heapify(maxHeap)
        
        for _ in range(k):
            pile = heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, pile - math.ceil(pile/2))
            
        return sum([-heapq.heappop(maxHeap) for _ in range(N)])'''

        # improved solution, simplify operations
        maxHeap = [-p for p in piles]
        heapq.heapify(maxHeap)
        for _ in range(k):
            # take smallest element, and push new item
            # floor division is the same as subtracting the ceiling result
            heapq.heapreplace(maxHeap, maxHeap[0] // 2)

        return -sum(maxHeap)



sol = Solution() 
