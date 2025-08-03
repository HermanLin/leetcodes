import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for point in points:
            x, y = point
            d = math.sqrt((x * x) + (y * y))
            heapq.heappush(heap, (-d, (x, y)))
            
            if len(heap) > k:
                heapq.heappop(heap)
                
        return [p[1] for p in heap]

sol = Solution() 
