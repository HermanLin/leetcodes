import heapq
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        '''heap = []
        for boxes, units in boxTypes:
            heapq.heappush(heap, (-units, boxes))
        
        totalBoxes, totalUnits = 0, 0
        while heap:
            units, boxes = heapq.heappop(heap)
            for _ in range(boxes):
                if totalBoxes + 1 > truckSize:
                    return totalUnits
                
                totalBoxes += 1
                totalUnits -= units
                
        return totalUnits'''

        '''# improved solution, reduce complexity
        heap = []
        for boxes, units in boxTypes:
            heapq.heappush(heap, (-units, boxes))
        
        total = 0
        while heap:
            units, boxes = heapq.heappop(heap)
            if truckSize >= boxes:
                truckSize -= boxes
                total += boxes * -units
            else:
                total += truckSize * -units
                break
                
        return total'''

        # improved solution, remove O(n) space
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        total = 0
        for boxes, units in boxTypes:
            if truckSize >= boxes:
                truckSize -= boxes
                total += boxes * units
            else:
                total += truckSize * units
                break

        return total

sol = Solution() 
print(sol.maximumUnits([[1,3],[2,2],[3,1]], 4))
print(sol.maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))
