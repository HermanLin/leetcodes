from typing import List


class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        N = len(weight)
        weight.sort()
        
        total = 0
        for i in range(N):
            total += weight[i]
            if total > 5000:
                return i
            
        return N

sol = Solution() 
