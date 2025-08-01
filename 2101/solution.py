from collections import defaultdict
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        N = len(bombs)
        graph = defaultdict(list)
        
        # pre-process the bombs into a graph
        for i in range(N):
            x, y, r = bombs[i]
            for j in range(N):
                if i != j:
                    a, b, c = bombs[j]
                    if (a - x)**2 + (b - y)**2 <= r**2:
                        graph[i].append(j)

        ans = 0

        for i in range(N):
            stack = [(i, set([i]))]

            while stack:
                bomb, boomed = stack.pop()

                ans = max(ans, len(boomed))
                bombs_in_range = graph[bomb]

                # how many more can we boom?
                will_boom = len(bombs_in_range) - sum(1 for b in bombs_in_range if b in boomed)

                for b in bombs_in_range:
                    if b not in boomed:
                        boomed.add(b)
                        stack.append((b, boomed))
                
        return ans
            
            

sol = Solution() 
