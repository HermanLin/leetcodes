import heapq
from typing import Counter, List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        '''N = len(arr)
        occurrences = Counter(arr)
        
        heap = []
        for num in occurrences:
            heapq.heappush(heap, -occurrences[num])
            
        ans, count = 0, 0
        while heap:
            count -= heapq.heappop(heap)
            
            if count < N / 2:
                ans += 1
            else:
                break
                
        return ans + 1'''

        # alternative solution
        occurrences = Counter(arr)

        sorted_count = sorted(occurrences.values(), reverse=True)

        target = len(arr) / 2
        ans, total = 0, 0
        for count in sorted_count:
            if total >= target:
                break
            ans += 1
            total += count

        return ans

sol = Solution() 
print(sol.minSetSize([3,3,3,3,5,5,5,2,2,7]))
print(sol.minSetSize([7,7,7,7,7,7]))
print(sol.minSetSize([7,6]))
