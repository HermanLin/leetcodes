from collections import defaultdict
from typing import List


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        # convert restricted into a set for faster checks
        # also use this as our "seen" set
        visited = set(restricted)
        
        # construct graph representation
        graph = defaultdict(list)
        for src, dest in edges:
            # simplify our graph to only connect unrestricted nodes together
            if src not in visited and dest not in visited:
                graph[src].append(dest)
                graph[dest].append(src) 
        
        visited.add(0)
        stack = [0]
        count = 1
        
        while stack:
            node = stack.pop()
            
            for n in graph[node]:
                if n not in visited:
                    count += 1
                    visited.add(n)
                    stack.append(n)
                    
        return count

sol = Solution() 
