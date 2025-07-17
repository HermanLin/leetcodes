import math
from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # use a map to store the last seen index of a matching card
        seen = {}
        minimum = math.inf

        N = len(cards)
        for i in range(N):
            if cards[i] not in seen:
                seen[cards[i]] = i
            else:
                minimum = min(minimum, i - seen[cards[i]] + 1)
                seen[cards[i]] = i
        
        if minimum == math.inf:
            return -1
        return int(minimum)
    
sol = Solution()
print(sol.minimumCardPickup([3,4,2,3,4,7]))
print(sol.minimumCardPickup([1,0,5,3]))
print(sol.minimumCardPickup([4,7,10,6,6,4,2,7,0,9,2,2,9,1,10,2,0,8,4,0]))
print(sol.minimumCardPickup([1]))