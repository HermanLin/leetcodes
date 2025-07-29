from collections import defaultdict
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # construct graph representation
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        # depth-first search to explore each connected component
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
            
        seen = set()
        ans = 0
        
        # go through each node and determine whether it's part of a component
        for node in range(n):
            if node not in seen:
                ans += 1
                seen.add(node)
                dfs(node)
                
        return ans
 
sol = Solution() 
print(sol.countComponents(5, [[0,1],[1,2],[3,4]]))
print(sol.countComponents(6, [[0,1],[1,2],[3,4]]))
print(sol.countComponents(5, [[0,1],[1,2],[2,3],[3,4]]))
print(sol.countComponents(10, [[0,1],[0,2],[0,3],[3,4],[0,4]]))
