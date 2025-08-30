from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        '''
        # the judge is the person with no outbound neighbors,
        # but also has n - 1 inbound neighbors
        outbound = defaultdict(int)
        inbound = defaultdict(int)

        for a, b in trust:
            outbound[a] += 1
            inbound[b] += 1

        judge = -1
        for i in range(1, n + 1):
            if not outbound[i] and inbound[i] == n-1:
                if judge != -1:
                    # multiple judges present
                    return -1
                judge = i
            
        return judge
        '''

        # revised approach
        # inbound connections are positive
        # outbound connections are negative
        connections = [0] * n

        for a, b in trust:
            connections[a-1] -= 1
            connections[b-1] += 1

        for i in range(n):
            if connections[i] == n-1:
                return i+1
        
        return -1


sol = Solution() 
